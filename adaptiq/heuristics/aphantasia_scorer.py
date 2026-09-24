"""Aphantasia Heuristic Scoring Engine based on PRD Section 3.2."""

from __future__ import annotations

from typing import Any


class AphantasiaScorer:
    """Computes imagery score deltas and confidence metrics based on behavioral signals."""

    def compute_delta(
        self,
        current_score: float,
        interaction_log: list[dict[str, Any]],
        report: dict[str, Any],
    ) -> tuple[float, float, float]:
        """Compute (new_score, delta, confidence) using PRD Section 3.2 rules.

        Returns:
            new_score (float): Clamped to [0.0, 10.0]
            delta (float): Clamped per-session delta in range [-2.0, 2.0]
            confidence (float): Metric between 0.0 and 1.0
        """
        # Guardrail: Insufficient interaction events
        if len(interaction_log) < 3:
            return current_score, 0.0, 0.2

        delta = 0.0
        confidence_points = 0.0

        # Signal 1: Spatial metaphor confusion events
        spatial_confusion = sum(
            1
            for ev in interaction_log
            if ev.get("event_type") == "confusion_signal"
            and ev.get("metaphor_type") == "spatial"
        )
        delta -= spatial_confusion * 0.5
        confidence_points += spatial_confusion

        # Signal 2: Formal syntax / trace table fast-pass events
        formal_success = sum(
            1
            for ev in interaction_log
            if ev.get("event_type") == "fast_pass"
            and ev.get("metaphor_type") == "formal"
        )
        delta -= formal_success * 0.3
        confidence_points += formal_success

        # Signal 3: Divergence in assessment section scores
        eval_dict = report.get("submission_evaluation", report)
        section_scores = eval_dict.get("section_scores", {})
        spatial_score = section_scores.get("spatial_analogy_questions", 1.0)
        trace_score = section_scores.get("trace_table_questions", 0.0)

        divergence = False
        if spatial_score < 0.5 and trace_score >= 0.8:
            delta -= 1.5
            confidence_points += 3.0
            divergence = True

        # Clamp max delta per session to [-2.0, 2.0]
        clamped_delta = max(-2.0, min(2.0, delta))
        confidence = min(1.0, (confidence_points + 2.0) / 8.0)

        # If confidence is below threshold and no strong signals, hold score
        if confidence < 0.4 and not divergence:
            return current_score, 0.0, confidence

        new_score = max(0.0, min(10.0, current_score + clamped_delta))
        return round(new_score, 2), round(clamped_delta, 2), round(confidence, 2)
