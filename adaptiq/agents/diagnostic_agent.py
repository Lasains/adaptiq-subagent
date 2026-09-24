"""Cognitive Diagnostic & Profiling Agent (The Observer)."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Any, Optional
from pydantic import BaseModel, Field

from adaptiq.heuristics.aphantasia_scorer import AphantasiaScorer
from adaptiq.state.learner_profile import LearnerProfile
from adaptiq.tools.misconception_tracker import MisconceptionTracker


class DiagnosticAgentInput(BaseModel):
    session_id: str
    learner_id: str
    assessment_report: dict[str, Any]
    interaction_log: list[dict[str, Any]] = Field(default_factory=list)
    current_profile: LearnerProfile


class DiagnosticPayload(BaseModel):
    session_id: str
    learner_id: str
    chapter_assessed: int
    topic: str
    score_delta: float
    updated_visual_imagery_score: float
    diagnostic_confidence: float
    new_misconceptions: list[str]
    resolved_misconceptions: list[str]
    updated_current_misconceptions: list[str]
    recommended_modality: str
    remediation_required: bool
    reasoning_summary: str


class DiagnosticAgent:
    """Heuristic cognitive profiler detecting learner abstraction preferences and Aphantasia signals."""

    def __init__(
        self,
        scorer: Optional[AphantasiaScorer] = None,
        tracker: Optional[MisconceptionTracker] = None,
    ):
        self.scorer = scorer or AphantasiaScorer()
        self.tracker = tracker or MisconceptionTracker()

    async def update_profile(
        self, agent_input: DiagnosticAgentInput
    ) -> tuple[DiagnosticPayload, LearnerProfile]:
        eval_result = agent_input.assessment_report.get("submission_evaluation", {})
        overall_score = eval_result.get("overall_score", 1.0)
        chapter = agent_input.assessment_report.get("chapter", 1)
        topic = agent_input.assessment_report.get("topic", "General JavaScript")

        current_traits = agent_input.current_profile.cognitive_traits
        current_score = current_traits.visual_imagery_score

        new_score, delta, confidence = self.scorer.compute_delta(
            current_score=current_score,
            interaction_log=agent_input.interaction_log,
            report=agent_input.assessment_report,
        )

        # Misconception tracking delta
        error_taxonomy = eval_result.get("error_taxonomy", [])
        new_misconceptions, resolved_misconceptions, active_misconceptions = (
            self.tracker.compute_delta(
                current_misconceptions=agent_input.current_profile.current_misconceptions,
                error_taxonomy=error_taxonomy,
                overall_score=overall_score,
            )
        )

        # Determine recommended modality
        if new_score <= 3.0:
            recommended_modality = "aphantasia_adapted"
        elif new_score >= 8.0:
            recommended_modality = "hyper_visual"
        else:
            recommended_modality = "standard"

        remediation_required = overall_score < 0.60

        # Build payload
        payload = DiagnosticPayload(
            session_id=agent_input.session_id,
            learner_id=agent_input.learner_id,
            chapter_assessed=chapter,
            topic=topic,
            score_delta=round(delta, 2),
            updated_visual_imagery_score=round(new_score, 2),
            diagnostic_confidence=round(confidence, 2),
            new_misconceptions=new_misconceptions,
            resolved_misconceptions=resolved_misconceptions,
            updated_current_misconceptions=active_misconceptions,
            recommended_modality=recommended_modality,
            remediation_required=remediation_required,
            reasoning_summary=f"Processed {len(agent_input.interaction_log)} events with delta {delta:.2f}.",
        )

        # Clone and update profile
        updated_profile = agent_input.current_profile.model_copy(deep=True)
        updated_profile.updated_at = datetime.now(timezone.utc).isoformat()
        updated_profile.diagnostic_confidence = round(confidence, 2)
        updated_profile.current_misconceptions = active_misconceptions
        updated_profile.resolved_misconceptions.extend(
            [r for r in resolved_misconceptions if r not in updated_profile.resolved_misconceptions]
        )

        updated_profile.cognitive_traits.visual_imagery_score = round(new_score, 2)
        updated_profile.cognitive_traits.visual_imagery_score_history.append(round(new_score, 2))
        updated_profile.cognitive_traits.preferred_explanation_modality = recommended_modality

        if new_score <= 3.0:
            updated_profile.cognitive_traits.abstraction_preference = "formal_symbolic"

        # Update indicators
        spatial_evs = sum(
            1
            for ev in agent_input.interaction_log
            if ev.get("metaphor_type") == "spatial"
        )
        formal_evs = sum(
            1
            for ev in agent_input.interaction_log
            if ev.get("metaphor_type") == "formal"
        )
        updated_profile.aphantasia_indicators.spatial_metaphor_confusion_events += spatial_evs
        updated_profile.aphantasia_indicators.formal_syntax_high_comprehension_events += formal_evs
        updated_profile.aphantasia_indicators.score_delta_last_3_sessions = round(delta, 2)

        return payload, updated_profile
