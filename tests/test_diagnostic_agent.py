"""Tests for DiagnosticAgent, AphantasiaScorer, and MisconceptionTracker."""

import pytest

from adaptiq.agents.diagnostic_agent import DiagnosticAgent, DiagnosticAgentInput, DiagnosticPayload
from adaptiq.heuristics.aphantasia_scorer import AphantasiaScorer
from adaptiq.state.learner_profile import DEFAULT_PROFILE, LearnerProfile


@pytest.fixture
def aphantasia_scorer():
    return AphantasiaScorer()


@pytest.fixture
def diagnostic_agent():
    return DiagnosticAgent()


def test_scorer_delta_calculations(aphantasia_scorer):
    # 2 spatial confusion events: -0.5 * 2 = -1.0
    # 1 formal fast-pass: -0.3 * 1 = -0.3
    # divergence: spatial < 0.5 and trace >= 0.8: -1.5
    # Total delta = -2.8, clamped to max decrease of -2.0
    interaction_log = [
        {"timestamp": "2026-09-24T10:00:00Z", "event_type": "confusion_signal", "metaphor_type": "spatial"},
        {"timestamp": "2026-09-24T10:01:00Z", "event_type": "confusion_signal", "metaphor_type": "spatial"},
        {"timestamp": "2026-09-24T10:02:00Z", "event_type": "fast_pass", "metaphor_type": "formal"},
    ]
    report = {
        "submission_evaluation": {
            "section_scores": {
                "spatial_analogy_questions": 0.3,
                "trace_table_questions": 0.9,
            }
        }
    }
    new_score, delta, confidence = aphantasia_scorer.compute_delta(
        current_score=5.0, interaction_log=interaction_log, report=report
    )
    assert delta == -2.0  # clamped from -2.8 to -2.0
    assert new_score == 3.0
    assert confidence > 0.4


def test_guardrail_insufficient_log(aphantasia_scorer):
    # Less than 3 events
    interaction_log = [
        {"timestamp": "2026-09-24T10:00:00Z", "event_type": "confusion_signal", "metaphor_type": "spatial"}
    ]
    report = {
        "submission_evaluation": {
            "section_scores": {
                "spatial_analogy_questions": 0.2,
                "trace_table_questions": 0.9,
            }
        }
    }
    new_score, delta, confidence = aphantasia_scorer.compute_delta(
        current_score=5.0, interaction_log=interaction_log, report=report
    )
    assert delta == 0.0
    assert new_score == 5.0
    assert confidence == 0.2


@pytest.mark.asyncio
async def test_misconception_tracking_and_resolution(diagnostic_agent):
    profile = DEFAULT_PROFILE.model_copy(deep=True)
    profile.current_misconceptions = ["existing_concept_error"]

    # 1. First report introduces new error, score is 0.50 (< 0.85)
    report1 = {
        "chapter": 1,
        "topic": "JavaScript Closures",
        "submission_evaluation": {
            "overall_score": 0.50,
            "section_scores": {
                "spatial_analogy_questions": 0.4,
                "trace_table_questions": 0.85,
            },
            "error_taxonomy": [
                {
                    "error_type": "conceptual_misunderstanding",
                    "concept_area": "lexical_environment_retention",
                    "description": "Outer scope destroyed",
                    "materi_reference": "§2",
                    "actionable_feedback": "Review trace",
                }
            ],
        },
    }
    log = [
        {"event_type": "confusion_signal", "metaphor_type": "spatial"},
        {"event_type": "fast_pass", "metaphor_type": "formal"},
        {"event_type": "fast_pass", "metaphor_type": "formal"},
    ]
    inp1 = DiagnosticAgentInput(
        session_id="sess_diag_01",
        learner_id=profile.learner_id,
        assessment_report=report1,
        interaction_log=log,
        current_profile=profile,
    )
    payload1, updated_profile1 = await diagnostic_agent.update_profile(inp1)
    assert "lexical_environment_retention" in payload1.new_misconceptions
    assert "lexical_environment_retention" in updated_profile1.current_misconceptions
    assert "existing_concept_error" in updated_profile1.current_misconceptions

    # 2. Second report achieves pass (overall_score = 0.90 >= 0.85)
    report2 = {
        "chapter": 2,
        "topic": "JavaScript Closures",
        "submission_evaluation": {
            "overall_score": 0.90,
            "section_scores": {
                "spatial_analogy_questions": 0.4,
                "trace_table_questions": 0.95,
            },
            "error_taxonomy": [],
        },
    }
    inp2 = DiagnosticAgentInput(
        session_id="sess_diag_01",
        learner_id=profile.learner_id,
        assessment_report=report2,
        interaction_log=log,
        current_profile=updated_profile1,
    )
    payload2, updated_profile2 = await diagnostic_agent.update_profile(inp2)
    assert len(payload2.resolved_misconceptions) > 0
    assert len(updated_profile2.current_misconceptions) == 0


@pytest.mark.asyncio
async def test_multi_session_convergence_to_aphantasia(diagnostic_agent):
    profile = DEFAULT_PROFILE.model_copy(deep=True)
    assert profile.cognitive_traits.visual_imagery_score == 5.0

    aphantasia_log = [
        {"event_type": "confusion_signal", "metaphor_type": "spatial"},
        {"event_type": "confusion_signal", "metaphor_type": "spatial"},
        {"event_type": "fast_pass", "metaphor_type": "formal"},
    ]
    report = {
        "chapter": 1,
        "topic": "JavaScript Closures",
        "submission_evaluation": {
            "overall_score": 0.70,
            "section_scores": {
                "spatial_analogy_questions": 0.3,
                "trace_table_questions": 0.9,
            },
            "error_taxonomy": [],
        },
    }

    # Session 1
    inp1 = DiagnosticAgentInput(
        session_id="sess_conv_01",
        learner_id=profile.learner_id,
        assessment_report=report,
        interaction_log=aphantasia_log,
        current_profile=profile,
    )
    payload1, profile = await diagnostic_agent.update_profile(inp1)
    assert profile.cognitive_traits.visual_imagery_score == 3.0
    assert payload1.recommended_modality == "aphantasia_adapted"

    # Session 2
    report["chapter"] = 2
    inp2 = DiagnosticAgentInput(
        session_id="sess_conv_01",
        learner_id=profile.learner_id,
        assessment_report=report,
        interaction_log=aphantasia_log,
        current_profile=profile,
    )
    payload2, profile = await diagnostic_agent.update_profile(inp2)
    assert profile.cognitive_traits.visual_imagery_score == 1.0
    assert profile.cognitive_traits.visual_imagery_score <= 3.0
    assert profile.cognitive_traits.preferred_explanation_modality == "aphantasia_adapted"
    assert profile.cognitive_traits.abstraction_preference == "formal_symbolic"
