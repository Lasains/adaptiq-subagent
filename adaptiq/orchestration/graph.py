"""LangGraph StateGraph orchestration engine linking all AdaptIQ subagents."""

from __future__ import annotations

import json
from typing import Any, Optional, TypedDict
from langgraph.graph import END, START, StateGraph

from adaptiq.agents.assessment_agent import AssessmentAgent, ChallengeSpec
from adaptiq.agents.diagnostic_agent import DiagnosticAgent, DiagnosticAgentInput
from adaptiq.agents.tutor_agent import TutorAgent, TutorAgentInput
from adaptiq.filesystem.artifact_manager import ArtifactManager
from adaptiq.state.blackboard import BlackboardState, BlackboardStore
from adaptiq.state.learner_profile import DEFAULT_PROFILE, LearnerProfile, ProfileStore


class OrchestrationState(TypedDict, total=False):
    session_id: str
    learner_id: str
    topic: str
    chapter: int
    attempt_count: int
    remediation_mode: bool
    escalation_flag: bool
    learner_profile: Optional[LearnerProfile]
    materi_text: str
    challenges: list[dict[str, Any]]
    submission_code: str
    interaction_log: list[dict[str, Any]]
    assessment_report: dict[str, Any]
    diagnostic_payload: dict[str, Any]
    pass_fail: str
    terminated: bool


def remediation_router(state: OrchestrationState) -> str:
    """Evaluate assessment status and route to appropriate next node."""
    pass_fail = state.get("pass_fail", "fail")
    attempt = state.get("attempt_count", 1)

    if pass_fail == "pass":
        return "advance_chapter"
    elif pass_fail == "partial_pass":
        return "challenge_generation"
    else:
        if attempt >= 3:
            return "escalation"
        return "tutor_remediation"


class AdaptIQOrchestrator:
    """Coordinates subagents, persistence, and state transitions using LangGraph."""

    def __init__(
        self,
        blackboard_store: Optional[BlackboardStore] = None,
        profile_store: Optional[ProfileStore] = None,
        artifact_manager: Optional[ArtifactManager] = None,
        tutor_agent: Optional[TutorAgent] = None,
        assessment_agent: Optional[AssessmentAgent] = None,
        diagnostic_agent: Optional[DiagnosticAgent] = None,
    ):
        self.blackboard_store = blackboard_store or BlackboardStore()
        self.profile_store = profile_store or ProfileStore()
        self.artifact_manager = artifact_manager or ArtifactManager()
        self.tutor_agent = tutor_agent or TutorAgent()
        self.assessment_agent = assessment_agent or AssessmentAgent()
        self.diagnostic_agent = diagnostic_agent or DiagnosticAgent()

        self.graph = build_orchestration_graph(self)

    async def diagnostic_context_inject_node(
        self, state: OrchestrationState
    ) -> dict[str, Any]:
        session_id = state.get("session_id", "default_session")
        learner_id = state.get("learner_id", "default_learner")
        topic = state.get("topic", "JavaScript Asynchronous Event Loop")

        # Load or init Blackboard
        bb = await self.blackboard_store.get_or_create(
            session_id=session_id, learner_id=learner_id, topic=topic
        )

        # Load or init Profile
        profile = state.get("learner_profile")
        if profile is None:
            profile = await self.profile_store.load(learner_id)

        chapter = state.get("chapter", bb.current_chapter)
        attempt_count = state.get("attempt_count", bb.attempt_count)
        remediation_mode = state.get("remediation_mode", bb.remediation_triggered)

        return {
            "session_id": session_id,
            "learner_id": learner_id,
            "topic": topic,
            "chapter": chapter,
            "attempt_count": attempt_count,
            "remediation_mode": remediation_mode,
            "learner_profile": profile,
            "escalation_flag": bb.escalation_flag,
        }

    async def tutor_agent_node(self, state: OrchestrationState) -> dict[str, Any]:
        profile = state.get("learner_profile") or DEFAULT_PROFILE
        tutor_input = TutorAgentInput(
            session_id=state.get("session_id", "default_session"),
            topic=state.get("topic", "JavaScript Asynchronous Event Loop"),
            chapter_number=state.get("chapter", 1),
            prerequisites=["call stack", "synchronous execution"],
            learner_profile=profile,
            previous_misconceptions=profile.current_misconceptions,
            remediation_mode=state.get("remediation_mode", False),
        )

        materi_md = await self.tutor_agent.generate_material(tutor_input)

        # Persist artifact
        await self.artifact_manager.write_artifact(
            state.get("session_id", "default_session"), "materi.md", materi_md
        )

        return {"materi_text": materi_md}

    async def challenge_generation_node(
        self, state: OrchestrationState
    ) -> dict[str, Any]:
        profile = state.get("learner_profile") or DEFAULT_PROFILE
        materi_text = state.get("materi_text", "")
        chapter = state.get("chapter", 1)
        topic = state.get("topic", "JavaScript Asynchronous Event Loop")

        challenges = await self.assessment_agent.generate_challenges(
            materi_text=materi_text,
            profile=profile,
            chapter=chapter,
            topic=topic,
        )

        challenges_data = [c.model_dump() for c in challenges]

        # Format challenge.md for learner
        challenge_md_lines = [f"# Chapter {chapter} Challenges: {topic}\n"]
        for idx, ch in enumerate(challenges, start=1):
            challenge_md_lines.append(f"## Challenge {idx}: {ch.id} ({ch.type})")
            challenge_md_lines.append(f"**Difficulty:** {ch.difficulty}\n")
            challenge_md_lines.append(f"{ch.prompt}\n")
            if ch.code_snippet:
                challenge_md_lines.append(f"```javascript\n{ch.code_snippet}\n```\n")

        await self.artifact_manager.write_artifact(
            state.get("session_id", "default_session"),
            "challenge.md",
            "\n".join(challenge_md_lines),
        )

        return {"challenges": challenges_data}

    async def submission_eval_node(self, state: OrchestrationState) -> dict[str, Any]:
        challenges_dicts = state.get("challenges", [])
        challenges = [ChallengeSpec.model_validate(c) for c in challenges_dicts]

        submission_code = state.get("submission_code", "")
        session_id = state.get("session_id", "default_session")
        chapter = state.get("chapter", 1)
        topic = state.get("topic", "JavaScript Asynchronous Event Loop")

        report = await self.assessment_agent.evaluate_submission(
            session_id=session_id,
            chapter=chapter,
            topic=topic,
            submission_code=submission_code,
            challenges=challenges,
        )

        await self.artifact_manager.write_artifact(
            session_id, "assessment_report.json", json.dumps(report, indent=2)
        )

        overall_score = report.get("submission_evaluation", {}).get("overall_score", 0.0)
        pass_fail = report.get("submission_evaluation", {}).get("pass_fail", "fail")

        await self.blackboard_store.update(
            session_id,
            last_assessment_score=overall_score,
        )

        return {
            "assessment_report": report,
            "pass_fail": pass_fail,
        }

    async def diagnostic_update_node(
        self, state: OrchestrationState
    ) -> dict[str, Any]:
        session_id = state.get("session_id", "default_session")
        learner_id = state.get("learner_id", "default_learner")
        report = state.get("assessment_report", {})
        log = state.get("interaction_log", [])
        profile = state.get("learner_profile") or DEFAULT_PROFILE

        diag_input = DiagnosticAgentInput(
            session_id=session_id,
            learner_id=learner_id,
            assessment_report=report,
            interaction_log=log,
            current_profile=profile,
        )

        payload, updated_profile = await self.diagnostic_agent.update_profile(diag_input)

        await self.artifact_manager.write_artifact(
            session_id,
            "learner_profile.json",
            json.dumps(updated_profile.model_dump(), indent=2),
        )

        await self.profile_store.save(updated_profile)

        await self.blackboard_store.update(
            session_id,
            pending_diagnostic_payload=payload.model_dump(),
        )

        return {
            "learner_profile": updated_profile,
            "diagnostic_payload": payload.model_dump(),
        }

    async def advance_chapter_node(
        self, state: OrchestrationState
    ) -> dict[str, Any]:
        session_id = state.get("session_id", "default_session")
        new_chapter = state.get("chapter", 1) + 1

        await self.blackboard_store.update(
            session_id,
            current_chapter=new_chapter,
            attempt_count=1,
            remediation_triggered=False,
        )

        return {
            "chapter": new_chapter,
            "attempt_count": 1,
            "remediation_mode": False,
        }

    async def tutor_remediation_node(
        self, state: OrchestrationState
    ) -> dict[str, Any]:
        session_id = state.get("session_id", "default_session")
        attempt_count = state.get("attempt_count", 1) + 1

        await self.blackboard_store.update(
            session_id,
            attempt_count=attempt_count,
            remediation_triggered=True,
        )

        return {
            "attempt_count": attempt_count,
            "remediation_mode": True,
        }

    async def escalation_node(self, state: OrchestrationState) -> dict[str, Any]:
        session_id = state.get("session_id", "default_session")
        await self.blackboard_store.update(session_id, escalation_flag=True)

        return {
            "escalation_flag": True,
            "terminated": True,
        }

    async def run_cycle(self, initial_state: OrchestrationState) -> OrchestrationState:
        """Run an end-to-end orchestration cycle."""
        result = await self.graph.ainvoke(initial_state)
        return result


def build_orchestration_graph(orchestrator: AdaptIQOrchestrator):
    """Build LangGraph StateGraph mapping pedagogical lifecycle and remediation routing."""
    workflow = StateGraph(OrchestrationState)

    workflow.add_node("diagnostic_context_inject", orchestrator.diagnostic_context_inject_node)
    workflow.add_node("tutor_agent", orchestrator.tutor_agent_node)
    workflow.add_node("challenge_generation", orchestrator.challenge_generation_node)
    workflow.add_node("submission_eval", orchestrator.submission_eval_node)
    workflow.add_node("diagnostic_update", orchestrator.diagnostic_update_node)
    workflow.add_node("advance_chapter", orchestrator.advance_chapter_node)
    workflow.add_node("tutor_remediation", orchestrator.tutor_remediation_node)
    workflow.add_node("escalation", orchestrator.escalation_node)

    # Core linear backbone
    workflow.add_edge(START, "diagnostic_context_inject")
    workflow.add_edge("diagnostic_context_inject", "tutor_agent")
    workflow.add_edge("tutor_agent", "challenge_generation")
    workflow.add_edge("challenge_generation", "submission_eval")
    workflow.add_edge("submission_eval", "diagnostic_update")

    # Conditional router
    workflow.add_conditional_edges(
        "diagnostic_update",
        remediation_router,
        {
            "advance_chapter": "advance_chapter",
            "challenge_generation": "challenge_generation",
            "tutor_remediation": "tutor_remediation",
            "escalation": "escalation",
        },
    )

    # Termination and loops
    workflow.add_edge("advance_chapter", END)
    workflow.add_edge("escalation", END)
    workflow.add_edge("tutor_remediation", "tutor_agent")

    return workflow.compile()
