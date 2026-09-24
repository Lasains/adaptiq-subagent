"""Misconception tracking and resolution engine."""

from __future__ import annotations

from typing import Any


class MisconceptionTracker:
    """Tracks novel concept errors and marks mastered concepts as resolved."""

    def compute_delta(
        self,
        current_misconceptions: list[str],
        error_taxonomy: list[dict[str, Any]],
        overall_score: float,
    ) -> tuple[list[str], list[str], list[str]]:
        """Compute (new_misconceptions, resolved_misconceptions, active_misconceptions)."""
        new_misconceptions: list[str] = []
        for err in error_taxonomy:
            concept = err.get("concept_area", "")
            if concept and concept not in current_misconceptions and concept not in new_misconceptions:
                new_misconceptions.append(concept)

        resolved_misconceptions: list[str] = []
        if overall_score >= 0.85:
            # High-pass threshold resolves active misconceptions tested in this cycle
            resolved_misconceptions = list(current_misconceptions)

        active = [
            m
            for m in (current_misconceptions + new_misconceptions)
            if m not in resolved_misconceptions
        ]

        return new_misconceptions, resolved_misconceptions, active
