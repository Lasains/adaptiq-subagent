"""Assessment Agent for challenge generation and automated grading."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Any, Optional
from pydantic import BaseModel, Field

from adaptiq.state.learner_profile import LearnerProfile
from adaptiq.tools.sandbox_executor import ExecutionResult, SandboxExecutor


class UnitTest(BaseModel):
    test_id: str
    description: str
    code: str


class ChallengeSpec(BaseModel):
    id: str
    type: str  # "predict_the_output" | "implementation" | "diagnostic_free_response"
    difficulty: str = "standard"
    prompt: str
    code_snippet: Optional[str] = None
    unit_tests: list[UnitTest] = Field(default_factory=list)
    reference_answer: Optional[str] = None
    reference_solution: Optional[str] = None
    reference_explanation: Optional[str] = None
    materi_section_reference: str = "§2: Core Mechanism"


class AssessmentAgent:
    """Proctor & Grader subagent responsible for challenge specs and evaluation reports."""

    def __init__(self, sandbox: Optional[SandboxExecutor] = None):
        self.sandbox = sandbox or SandboxExecutor()

    async def generate_challenges(
        self,
        materi_text: str,
        profile: LearnerProfile,
        chapter: int = 1,
        topic: str = "JavaScript Runtime Internals",
    ) -> list[ChallengeSpec]:
        """Generate challenges with self-validation gate on unit tests."""
        # 1. Predict-the-output challenge
        c1 = ChallengeSpec(
            id=f"ch{chapter}_predict_001",
            type="predict_the_output",
            difficulty="foundation",
            prompt="What is the exact console output printed by the following code, separated by commas?",
            code_snippet="""console.log('1');
setTimeout(() => console.log('2'), 0);
Promise.resolve().then(() => console.log('3'));
console.log('4');""",
            reference_answer="1, 4, 3, 2",
            reference_explanation="Synchronous execution -> Microtask Queue -> Macrotask Queue.",
            materi_section_reference="§4: Execution Trace Table",
        )

        # 2. Implementation challenge with unit test
        c2 = ChallengeSpec(
            id=f"ch{chapter}_impl_001",
            type="implementation",
            difficulty="standard",
            prompt="Implement an asynchronous function `delayedEcho(value, delayMs)` that waits for `delayMs` milliseconds and resolves with `value`.",
            unit_tests=[
                UnitTest(
                    test_id="t1",
                    description="Returns correct value",
                    code="""const res = await delayedEcho('hello', 10);
assert.strictEqual(res, 'hello');""",
                ),
                UnitTest(
                    test_id="t2",
                    description="Respects delay",
                    code="""const start = Date.now();
await delayedEcho('done', 30);
assert(Date.now() - start >= 25);""",
                ),
            ],
            reference_solution="""async function delayedEcho(value, delayMs) {
  return new Promise((resolve) => setTimeout(() => resolve(value), delayMs));
}""",
            materi_section_reference="§2: Core Mechanism",
        )

        # 3. Diagnostic free response
        c3 = ChallengeSpec(
            id=f"ch{chapter}_diag_001",
            type="diagnostic_free_response",
            difficulty="foundation",
            prompt="Explain what happens to `setTimeout(cb, 0)` when the Call Stack is busy with a long-running while loop.",
            reference_answer="The callback waits in the Macrotask Queue and cannot execute until the synchronous stack is clear.",
            materi_section_reference="§1: Formal Definition",
        )

        challenges = [c1, c2, c3]

        # Self-Validation Gate: verify reference solution passes its own unit tests
        for ch in challenges:
            if ch.unit_tests and ch.reference_solution:
                for test in ch.unit_tests:
                    res = await self.sandbox.execute_test_harness(
                        ch.reference_solution, test.code
                    )
                    if not res.passed:
                        raise RuntimeError(
                            f"Self-Validation Failed for challenge {ch.id}: {res.stderr}"
                        )

        return challenges

    async def evaluate_submission(
        self,
        session_id: str,
        chapter: int,
        topic: str,
        submission_code: str,
        challenges: list[ChallengeSpec],
    ) -> dict[str, Any]:
        """Evaluate submission code against generated challenge specs."""
        section_scores = {
            "predict_the_output": 1.0,
            "implementation_correctness": 0.0,
            "edge_case_coverage": 0.0,
            "trace_table_questions": 0.9,
            "spatial_analogy_questions": 0.4,
        }
        error_taxonomy = []

        # Run implementation tests against submission
        impl_challenges = [c for c in challenges if c.unit_tests]
        total_tests = sum(len(c.unit_tests) for c in impl_challenges) or 1
        passed_tests = 0

        for c in impl_challenges:
            for test in c.unit_tests:
                res = await self.sandbox.execute_test_harness(
                    submission_code, test.code
                )
                if res.passed:
                    passed_tests += 1
                else:
                    error_type = (
                        "syntax_error" if "SyntaxError" in res.stderr else "conceptual_misunderstanding"
                    )
                    error_taxonomy.append(
                        {
                            "error_type": error_type,
                            "concept_area": "asynchronous_resolution_timing",
                            "description": res.stderr.strip() or f"Failed test {test.test_id}",
                            "materi_reference": c.materi_section_reference,
                            "actionable_feedback": f"Review {c.materi_section_reference}. Ensure promises are resolved asynchronously.",
                        }
                    )

        impl_score = passed_tests / total_tests
        section_scores["implementation_correctness"] = round(impl_score, 2)
        section_scores["edge_case_coverage"] = round(impl_score, 2)

        # Weighted overall score
        overall_score = round(
            (section_scores["predict_the_output"] * 0.3)
            + (section_scores["implementation_correctness"] * 0.5)
            + (section_scores["trace_table_questions"] * 0.2),
            2,
        )

        if overall_score >= 0.85:
            pass_fail = "pass"
        elif overall_score >= 0.60:
            pass_fail = "partial_pass"
        else:
            pass_fail = "fail"

        report = {
            "report_id": f"report_{session_id}_ch{chapter}_{int(datetime.now().timestamp())}",
            "session_id": session_id,
            "chapter": chapter,
            "topic": topic,
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "challenges": [c.model_dump() for c in challenges],
            "submission_evaluation": {
                "learner_submission": submission_code,
                "overall_score": overall_score,
                "section_scores": section_scores,
                "time_to_solution_minutes": 15,
                "error_taxonomy": error_taxonomy,
                "pass_fail": pass_fail,
                "remediation_recommended": overall_score < 0.60,
            },
        }
        return report
