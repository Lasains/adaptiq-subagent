"""Cognitive Diagnostic & Profiling Agent (The Observer)."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Any, Optional
from pydantic import BaseModel, Field

from adaptiq.state.learner_profile import LearnerProfile


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

    def compute_heuristic_score(
        self,
        current_score: float,
        interaction_log: list[dict[str, Any]],
        section_scores: dict[str, float],
    ) -> tuple[float, float, float]:
        """Compute (new_score, delta, confidence) using the PRD Section 3.2 Aphantasia heuristics."""
        delta = 0.0
        confidence_points = 0

        # Guardrail: Insufficient data
        if len(interaction_log) < 3:
            return current_score, 0.0, 0.2

        # Signal 1: Spatial metaphor confusion
        spatial_confusion = sum(
            1
            for ev in interaction_log
            if ev.get("event_type") == "confusion_signal"
            and ev.get("metaphor_type") == "spatial"
        )
        delta -= spatial_confusion * 0.5
        confidence_points += spatial_confusion

        # Signal 2: Formal syntax / trace table high comprehension
        formal_success = sum(
            1
            for ev in interaction_log
            if ev.get("event_type") == "fast_pass"
            and ev.get("metaphor_type") == "formal"
        )
        delta -= formal_success * 0.3
        confidence_points += formal_success

        # Signal 3: Divergence in assessment questions
        spatial_score = section_scores.get("spatial_analogy_questions", 1.0)
        trace_score = section_scores.get("trace_table_questions", 0.0)
        if spatial_score < 0.5 and trace_score >= 0.8:
            delta -= 1.5
            confidence_points += 3

        # Clamp max decrease per session to 2.0
        delta = max(delta, -2.0)
        confidence = min(1.0, confidence_points / 8.0)

        if confidence < 0.4:
            # Not enough strong signals to justify changing the profile score
            return current_score, 0.0, confidence

        new_score = max(0.0, min(10.0, current_score + delta))
        return new_score, delta, confidence

    async def update_profile(
        self, agent_input: DiagnosticAgentInput
    ) -> tuple[DiagnosticPayload, LearnerProfile]:
        eval_result = agent_input.assessment_report.get("submission_evaluation", {})
        section_scores = eval_result.get("section_scores", {})
        overall_score = eval_result.get("overall_score", 1.0)
        chapter = agent_input.assessment_report.get("chapter", 1)
        topic = agent_input.assessment_report.get("topic", "General JavaScript")

        current_traits = agent_input.current_profile.cognitive_traits
        current_score = current_traits.visual_imagery_score

        new_score, delta, confidence = self.compute_heuristic_score(
            current_score, agent_input.interaction_log, section_scores
        )

        # Misconception tracking delta
        error_taxonomy = eval_result.get("error_taxonomy", [])
        new_misconceptions = [
            err.get("concept_area", "")
            for err in error_taxonomy
            if err.get("concept_area")
            and err.get("concept_area") not in agent_input.current_profile.current_misconceptions
        ]

        # Concept is resolved if overall score >= 0.85
        resolved_misconceptions = []
        if overall_score >= 0.85:
            resolved_misconceptions = list(agent_input.current_profile.current_misconceptions)

        active_misconceptions = [
            m
            for m in (agent_input.current_profile.current_misconceptions + new_misconceptions)
            if m not in resolved_misconceptions
        ]

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
        updated_profile.resolved_misconceptions.extend(resolved_misconceptions)

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
