"""End-to-End Pipeline & CLI Verification Tests."""

import re
import pytest
import yaml
from typer.testing import CliRunner

from adaptiq.cli.main import app
from adaptiq.filesystem.artifact_manager import ArtifactManager
from adaptiq.orchestration.graph import AdaptIQOrchestrator, OrchestrationState
from adaptiq.state.blackboard import BlackboardStore
from adaptiq.state.learner_profile import ProfileStore, create_default_profile

runner = CliRunner()


@pytest.fixture
def tmp_env(tmp_path, monkeypatch):
    db_path = str(tmp_path / "cli_test.db")
    session_dir = str(tmp_path / "sessions")
    curr_session_file = str(tmp_path / ".current_session")

    monkeypatch.setenv("ADAPTIQ_DB_PATH", db_path)
    monkeypatch.setenv("ADAPTIQ_SESSION_DIR", session_dir)
    monkeypatch.setenv("ADAPTIQ_SESSION_FILE", curr_session_file)

    return db_path, session_dir, curr_session_file


def test_cli_lifecycle(tmp_env, tmp_path):
    db_path, session_dir, curr_session_file = tmp_env

    # 1. adaptiq start
    result = runner.invoke(app, ["start", "--topic", "JavaScript Closures", "--session-id", "sess_cli_01"])
    assert result.exit_code == 0
    assert "sess_cli_01" in result.output
    assert "materi.md" in result.output

    # 2. adaptiq status
    status_result = runner.invoke(app, ["status", "--session-id", "sess_cli_01"])
    assert status_result.exit_code == 0
    assert "sess_cli_01" in status_result.output
    assert "JavaScript Closures" in status_result.output

    # 3. adaptiq submit
    sub_file = tmp_path / "my_submission.js"
    sub_file.write_text("async function delayedEcho(v, d) { return new Promise(r => setTimeout(() => r(v), d)); }", encoding="utf-8")
    submit_result = runner.invoke(app, ["submit", "--file", str(sub_file), "--session-id", "sess_cli_01"])
    assert submit_result.exit_code == 0
    assert "score" in submit_result.output.lower() or "assessment" in submit_result.output.lower()

    # 4. adaptiq next
    next_result = runner.invoke(app, ["next", "--session-id", "sess_cli_01"])
    assert next_result.exit_code == 0
    assert "Chapter 2" in next_result.output or "chapter" in next_result.output.lower()


@pytest.mark.asyncio
async def test_3_chapter_cognitive_adaptation_simulation(tmp_path):
    """Simulate a 3-chapter session on 'JavaScript Closures' validating cognitive adaptation.

    Chapter 1: Standard mode (score 5.0).
    Inject confusion -> Diagnostic agent drops score to 3.0.
    Chapter 2: score drops further to 1.0.
    Chapter 3: materi.md switches to 'aphantasia_adapted'.
    """
    db_path = str(tmp_path / "sim_pipeline.db")
    session_dir = str(tmp_path / "sessions")
    session_id = "sess_sim_dana_001"
    learner_id = "learner_dana_sim"
    topic = "JavaScript Closures"

    bb_store = BlackboardStore(db_path=db_path)
    profile_store = ProfileStore(db_path=db_path)
    artifact_mgr = ArtifactManager(base_dir=session_dir)

    orchestrator = AdaptIQOrchestrator(
        blackboard_store=bb_store,
        profile_store=profile_store,
        artifact_manager=artifact_mgr,
    )

    # Init profile with baseline score 5.0
    profile = create_default_profile(learner_id)
    assert profile.cognitive_traits.visual_imagery_score == 5.0
    await profile_store.save(profile)

    valid_solution = (
        "async function delayedEcho(val, ms) { "
        "  return new Promise(res => setTimeout(() => res(val), ms)); "
        "}"
    )

    # ---------------- CHAPTER 1 ----------------
    ch1_state: OrchestrationState = {
        "session_id": session_id,
        "learner_id": learner_id,
        "topic": topic,
        "chapter": 1,
        "attempt_count": 1,
        "remediation_mode": False,
        "submission_code": valid_solution,
        "interaction_log": [
            {"event_type": "confusion_signal", "metaphor_type": "spatial"},
            {"event_type": "confusion_signal", "metaphor_type": "spatial"},
            {"event_type": "fast_pass", "metaphor_type": "formal"},
        ],
    }

    res_ch1 = await orchestrator.run_cycle(ch1_state)
    assert res_ch1["pass_fail"] == "pass"

    # Verify Chapter 1 materi.md was generated with standard mode
    ch1_materi = await artifact_mgr.read_artifact(session_id, "materi.md")
    ch1_meta = yaml.safe_load(re.search(r"^---\n(.*?)\n---", ch1_materi, re.DOTALL).group(1))
    assert ch1_meta["cognitive_profile_applied"] == "standard"

    # Profile updated after Ch 1
    prof_ch1 = await profile_store.load(learner_id)
    assert prof_ch1.cognitive_traits.visual_imagery_score == 3.0  # dropped by 2.0

    # ---------------- CHAPTER 2 ----------------
    ch2_state: OrchestrationState = {
        "session_id": session_id,
        "learner_id": learner_id,
        "topic": topic,
        "chapter": 2,
        "attempt_count": 1,
        "remediation_mode": False,
        "submission_code": valid_solution,
        "interaction_log": [
            {"event_type": "confusion_signal", "metaphor_type": "spatial"},
            {"event_type": "confusion_signal", "metaphor_type": "spatial"},
            {"event_type": "fast_pass", "metaphor_type": "formal"},
        ],
    }

    res_ch2 = await orchestrator.run_cycle(ch2_state)
    assert res_ch2["pass_fail"] == "pass"

    # Profile updated after Ch 2
    prof_ch2 = await profile_store.load(learner_id)
    assert prof_ch2.cognitive_traits.visual_imagery_score <= 3.0
    assert prof_ch2.cognitive_traits.preferred_explanation_modality == "aphantasia_adapted"

    # ---------------- CHAPTER 3 ----------------
    ch3_state: OrchestrationState = {
        "session_id": session_id,
        "learner_id": learner_id,
        "topic": topic,
        "chapter": 3,
        "attempt_count": 1,
        "remediation_mode": False,
        "submission_code": valid_solution,
        "interaction_log": [
            {"event_type": "fast_pass", "metaphor_type": "formal"},
            {"event_type": "fast_pass", "metaphor_type": "formal"},
            {"event_type": "fast_pass", "metaphor_type": "formal"},
        ],
    }

    res_ch3 = await orchestrator.run_cycle(ch3_state)
    assert res_ch3["pass_fail"] == "pass"

    # Verify Chapter 3 materi.md switched to Aphantasia-Adapted mode!
    ch3_materi = await artifact_mgr.read_artifact(session_id, "materi.md")
    ch3_meta = yaml.safe_load(re.search(r"^---\n(.*?)\n---", ch3_materi, re.DOTALL).group(1))
    assert ch3_meta["cognitive_profile_applied"] == "aphantasia_adapted"

    # Forbidden words absent in Chapter 3
    lower_materi = ch3_materi.lower()
    for word in ["imagine", "visualize", "picture", "think of"]:
        assert word not in lower_materi

    # Trace table and state machine present
    assert "trace table" in lower_materi or "| step |" in lower_materi
    assert "state machine" in lower_materi or "state transition" in lower_materi

    # Score history confirms cognitive progression
    prof_ch3 = await profile_store.load(learner_id)
    assert prof_ch3.cognitive_traits.visual_imagery_score <= 3.0
    assert len(prof_ch3.cognitive_traits.visual_imagery_score_history) >= 3
