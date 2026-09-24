"""Tests for LangGraph StateGraph orchestration engine and remediation routing."""

import pytest

from adaptiq.filesystem.artifact_manager import ArtifactManager
from adaptiq.orchestration.graph import (
    AdaptIQOrchestrator,
    OrchestrationState,
    build_orchestration_graph,
    remediation_router,
)
from adaptiq.state.blackboard import BlackboardStore
from adaptiq.state.learner_profile import DEFAULT_PROFILE, ProfileStore


@pytest.fixture
def clean_stores(tmp_path):
    db_path = str(tmp_path / "test_graph.db")
    session_dir = str(tmp_path / "session")
    bb_store = BlackboardStore(db_path=db_path)
    profile_store = ProfileStore(db_path=db_path)
    artifact_mgr = ArtifactManager(base_dir=session_dir)
    return bb_store, profile_store, artifact_mgr


def test_remediation_router_branches():
    # 1. Pass -> advance_chapter
    state_pass: OrchestrationState = {
        "pass_fail": "pass",
        "attempt_count": 1,
        "escalation_flag": False,
    }
    assert remediation_router(state_pass) == "advance_chapter"

    # 2. Partial pass -> challenge_generation
    state_partial: OrchestrationState = {
        "pass_fail": "partial_pass",
        "attempt_count": 1,
        "escalation_flag": False,
    }
    assert remediation_router(state_partial) == "challenge_generation"

    # 3. Fail on attempt 1 -> tutor_remediation
    state_fail_1: OrchestrationState = {
        "pass_fail": "fail",
        "attempt_count": 1,
        "escalation_flag": False,
    }
    assert remediation_router(state_fail_1) == "tutor_remediation"

    # 4. Fail on attempt 2 -> tutor_remediation
    state_fail_2: OrchestrationState = {
        "pass_fail": "fail",
        "attempt_count": 2,
        "escalation_flag": False,
    }
    assert remediation_router(state_fail_2) == "tutor_remediation"

    # 5. Fail on attempt 3 -> escalation
    state_fail_3: OrchestrationState = {
        "pass_fail": "fail",
        "attempt_count": 3,
        "escalation_flag": False,
    }
    assert remediation_router(state_fail_3) == "escalation"


@pytest.mark.asyncio
async def test_orchestrator_pass_advances_chapter(clean_stores):
    bb_store, profile_store, artifact_mgr = clean_stores
    orchestrator = AdaptIQOrchestrator(
        blackboard_store=bb_store,
        profile_store=profile_store,
        artifact_manager=artifact_mgr,
    )

    # Initial blackboard
    await bb_store.get_or_create(
        session_id="sess_graph_pass",
        learner_id="learner_001",
        topic="JavaScript Scope",
    )

    # Valid submission code
    valid_code = "async function delayedEcho(v, d) { return new Promise(r => setTimeout(() => r(v), d)); }"
    init_state: OrchestrationState = {
        "session_id": "sess_graph_pass",
        "learner_id": "learner_001",
        "topic": "JavaScript Scope",
        "chapter": 1,
        "attempt_count": 1,
        "remediation_mode": False,
        "submission_code": valid_code,
        "interaction_log": [
            {"event_type": "fast_pass", "metaphor_type": "formal"},
            {"event_type": "fast_pass", "metaphor_type": "formal"},
            {"event_type": "fast_pass", "metaphor_type": "formal"},
        ],
    }

    final_state = await orchestrator.run_cycle(init_state)

    assert final_state.get("pass_fail") == "pass"
    assert final_state.get("chapter") == 2
    assert final_state.get("attempt_count") == 1

    # Check blackboard
    bb = await bb_store.read("sess_graph_pass")
    assert bb.current_chapter == 2
    assert bb.attempt_count == 1
    assert bb.last_assessment_score is not None


@pytest.mark.asyncio
async def test_orchestrator_escalation_on_third_failure(clean_stores):
    bb_store, profile_store, artifact_mgr = clean_stores
    orchestrator = AdaptIQOrchestrator(
        blackboard_store=bb_store,
        profile_store=profile_store,
        artifact_manager=artifact_mgr,
    )

    await bb_store.get_or_create(
        session_id="sess_graph_fail3",
        learner_id="learner_001",
        topic="JavaScript Scope",
    )
    await bb_store.update("sess_graph_fail3", attempt_count=3)

    broken_code = "const broken = ;"
    init_state: OrchestrationState = {
        "session_id": "sess_graph_fail3",
        "learner_id": "learner_001",
        "topic": "JavaScript Scope",
        "chapter": 1,
        "attempt_count": 3,
        "remediation_mode": True,
        "submission_code": broken_code,
        "interaction_log": [],
    }

    final_state = await orchestrator.run_cycle(init_state)

    assert final_state.get("escalation_flag") is True
    assert final_state.get("terminated") is True

    bb = await bb_store.read("sess_graph_fail3")
    assert bb.escalation_flag is True
