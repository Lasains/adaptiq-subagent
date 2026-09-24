"""Tests for AssessmentAgent, challenge generation, self-validation gate, and grading."""

import pytest

from adaptiq.agents.assessment_agent import (
    AssessmentAgent,
    AssessmentAgentInput,
    ChallengeSpec,
    EvaluationResult,
    UnitTest,
)
from adaptiq.state.learner_profile import DEFAULT_PROFILE
from adaptiq.tools.sandbox_executor import SandboxExecutor


@pytest.fixture
def assessment_agent():
    return AssessmentAgent()


@pytest.mark.asyncio
async def test_challenge_generation_types(assessment_agent):
    challenges = await assessment_agent.generate_challenges(
        materi_text="# Sample Topic",
        profile=DEFAULT_PROFILE,
        chapter=1,
        topic="JavaScript Event Loop",
    )
    assert len(challenges) >= 3

    types = [c.type for c in challenges]
    assert "predict_the_output" in types
    assert "implementation" in types
    assert "diagnostic_free_response" in types

    # Implementation challenge must have unit tests and reference solution
    impl = next(c for c in challenges if c.type == "implementation")
    assert len(impl.unit_tests) >= 1
    assert impl.reference_solution is not None


@pytest.mark.asyncio
async def test_self_validation_gate_broken_reference(assessment_agent):
    broken_challenge = ChallengeSpec(
        id="ch_broken",
        type="implementation",
        prompt="Broken challenge",
        unit_tests=[
            UnitTest(
                test_id="t1",
                description="Must fail",
                code="assert.strictEqual(brokenFunc(), 42);",
            )
        ],
        reference_solution="function brokenFunc() { return 0; }",  # returns 0 instead of 42
    )
    with pytest.raises(RuntimeError, match="Self-Validation Failed"):
        await assessment_agent.validate_challenge_reference(broken_challenge)


@pytest.mark.asyncio
async def test_evaluate_submission_perfect_pass(assessment_agent):
    challenges = await assessment_agent.generate_challenges(
        materi_text="# Sample",
        profile=DEFAULT_PROFILE,
        chapter=1,
        topic="JavaScript Event Loop",
    )
    impl = next(c for c in challenges if c.type == "implementation")
    correct_solution = impl.reference_solution

    result = await assessment_agent.evaluate_submission(
        session_id="sess_eval_001",
        chapter=1,
        topic="JavaScript Event Loop",
        submission_code=correct_solution,
        challenges=challenges,
    )
    eval_sub = result.get("submission_evaluation", {})
    assert eval_sub.get("pass_fail") == "pass"
    assert eval_sub.get("overall_score") >= 0.85
    assert len(eval_sub.get("error_taxonomy", [])) == 0
    assert eval_sub.get("remediation_recommended") is False


@pytest.mark.asyncio
async def test_evaluate_submission_syntax_error(assessment_agent):
    challenges = await assessment_agent.generate_challenges(
        materi_text="# Sample",
        profile=DEFAULT_PROFILE,
        chapter=1,
        topic="JavaScript Event Loop",
    )
    broken_syntax = "async function delayedEcho( { return ;"

    result = await assessment_agent.evaluate_submission(
        session_id="sess_eval_002",
        chapter=1,
        topic="JavaScript Event Loop",
        submission_code=broken_syntax,
        challenges=challenges,
    )
    eval_sub = result.get("submission_evaluation", {})
    assert eval_sub.get("pass_fail") == "fail"
    errors = eval_sub.get("error_taxonomy", [])
    assert len(errors) > 0
    assert any(err["error_type"] == "syntax_error" for err in errors)


@pytest.mark.asyncio
async def test_evaluate_submission_performance_issue(assessment_agent):
    challenges = await assessment_agent.generate_challenges(
        materi_text="# Sample",
        profile=DEFAULT_PROFILE,
        chapter=1,
        topic="JavaScript Event Loop",
    )
    infinite_loop = """async function delayedEcho(value, delayMs) {
      while(true) {}
    }"""

    # Use a small sandbox timeout for this test
    fast_agent = AssessmentAgent(sandbox=SandboxExecutor(default_timeout_seconds=1.0))
    result = await fast_agent.evaluate_submission(
        session_id="sess_eval_003",
        chapter=1,
        topic="JavaScript Event Loop",
        submission_code=infinite_loop,
        challenges=challenges,
    )
    eval_sub = result.get("submission_evaluation", {})
    errors = eval_sub.get("error_taxonomy", [])
    assert any(err["error_type"] == "performance_issue" for err in errors)


@pytest.mark.asyncio
async def test_evaluate_submission_edge_case_miss(assessment_agent):
    # Challenge with 2 tests: basic and edge case
    challenge = ChallengeSpec(
        id="ch_edge",
        type="implementation",
        prompt="Echo positive or throw",
        unit_tests=[
            UnitTest(
                test_id="t1_basic",
                description="Works on positive",
                code="assert.strictEqual(check(5), 5);",
            ),
            UnitTest(
                test_id="t2_edge",
                description="Throws on negative",
                code="assert.throws(() => check(-1));",
            ),
        ],
        reference_solution="function check(n) { if (n < 0) throw new Error(); return n; }",
    )
    # Submission handles positive but misses negative check
    submission = "function check(n) { return n; }"
    result = await assessment_agent.evaluate_submission(
        session_id="sess_eval_004",
        chapter=1,
        topic="JavaScript Errors",
        submission_code=submission,
        challenges=[challenge],
    )
    eval_sub = result.get("submission_evaluation", {})
    errors = eval_sub.get("error_taxonomy", [])
    assert len(errors) == 1
    assert errors[0]["error_type"] in ["edge_case_miss", "conceptual_misunderstanding"]
