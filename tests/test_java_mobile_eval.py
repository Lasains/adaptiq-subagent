"""Integration test and evaluation suite for Java Mobile Adaptive Tutor Subagent.
Validates subagent material and challenge generation for zero-knowledge beginners.
"""

import pytest
from tests.eval.eval_harness import JavaMobileEvalHarness


@pytest.fixture
def eval_harness():
    return JavaMobileEvalHarness()


@pytest.mark.asyncio
async def test_java_mobile_eval_benchmark_suite(eval_harness):
    """Run full benchmark evaluation on all 5 Java Mobile Zero-Knowledge cases."""
    results = await eval_harness.run_eval_suite()

    # Verify overall performance targets
    assert results["total_cases"] == 5
    assert results["all_passed"] is True, f"Some cases failed: {[c['case_id'] for c in results['cases'] if not c['passed']]}"
    assert results["total_score_percentage"] >= 90.0, f"Expected suite score >= 90%, got {results['total_score_percentage']}%"
    assert results["average_material_score"] >= 90.0, f"Expected material score >= 90%, got {results['average_material_score']}%"
    assert results["average_challenge_score"] >= 90.0, f"Expected challenge score >= 90%, got {results['average_challenge_score']}%"

    # Verify per-case criteria
    for case in results["cases"]:
        case_id = case["case_id"]
        mat_eval = case["material_evaluation"]
        ch_eval = case["challenge_evaluation"]

        # 1. Aphantasia Safety: 0 forbidden words and trace table present
        assert len(mat_eval["diagnostics"]["forbidden_words_found"]) == 0, f"Forbidden words found in {case_id}: {mat_eval['diagnostics']['forbidden_words_found']}"
        assert mat_eval["diagnostics"]["has_trace_table"] is True, f"Trace table missing in {case_id}"

        # 2. Executable Java Code
        assert mat_eval["diagnostics"]["code_executable"] is True, f"Java code execution failed in {case_id}: {mat_eval['diagnostics']['code_errors']}"

        # 3. Real-world physical analogy present for zero-knowledge beginners
        assert mat_eval["diagnostics"]["has_real_world_analogy"] is True, f"Real world analogy missing in {case_id}"

        # 4. Challenges: each case must have at least 3 foundation questions with answers and explanations
        assert ch_eval["diagnostics"]["challenge_count"] >= 3, f"Expected at least 3 challenges in {case_id}"
        assert ch_eval["diagnostics"]["has_reference_answers"] is True, f"Reference answers missing in {case_id}"
        assert ch_eval["diagnostics"]["has_explanations"] is True, f"Explanations missing in {case_id}"
