"""Typer CLI interface for AdaptIQ learning session operations."""

from __future__ import annotations

import asyncio
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Optional
import typer
from rich.console import Console
from rich.table import Table

from adaptiq.agents.assessment_agent import AssessmentAgent
from adaptiq.agents.diagnostic_agent import DiagnosticAgent, DiagnosticAgentInput
from adaptiq.agents.tutor_agent import TutorAgent, TutorAgentInput
from adaptiq.filesystem.artifact_manager import ArtifactManager
from adaptiq.state.blackboard import BlackboardStore
from adaptiq.state.learner_profile import ProfileStore

app = typer.Typer(help="AdaptIQ — Adaptive Multi-Agent Learning Platform CLI")
console = Console()


def get_paths():
    db_path = os.getenv("ADAPTIQ_DB_PATH", "adaptiq.db")
    session_dir = os.getenv("ADAPTIQ_SESSION_DIR", "./session")
    session_file = os.getenv("ADAPTIQ_SESSION_FILE", ".current_session")
    return db_path, session_dir, session_file


def save_current_session(session_id: str):
    _, _, session_file = get_paths()
    Path(session_file).write_text(session_id.strip(), encoding="utf-8")


def get_current_session(provided: Optional[str]) -> str:
    if provided:
        return provided
    _, _, session_file = get_paths()
    p = Path(session_file)
    if p.exists():
        s = p.read_text(encoding="utf-8").strip()
        if s:
            return s
    raise typer.BadParameter("No active session. Please specify --session-id or run `adaptiq start`.")


@app.command()
def start(
    topic: str = typer.Option("JavaScript Asynchronous Event Loop", "--topic", "-t", help="Topic to learn"),
    learner_id: str = typer.Option("learner_dana_7f3a", "--learner-id", "-l", help="Learner identifier"),
    session_id: Optional[str] = typer.Option(None, "--session-id", "-s", help="Unique session ID"),
):
    """Start a new adaptive learning session."""
    db_path, session_dir, _ = get_paths()

    if not session_id:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        session_id = f"sess_{timestamp}_{learner_id[:6]}"

    async def _start():
        bb_store = BlackboardStore(db_path=db_path)
        profile_store = ProfileStore(db_path=db_path)
        artifact_mgr = ArtifactManager(base_dir=session_dir)

        try:
            # 1. Initialize Blackboard & Profile
            bb = await bb_store.get_or_create(session_id=session_id, learner_id=learner_id, topic=topic)
            profile = await profile_store.load(learner_id)

            # 2. Generate initial materi.md
            tutor = TutorAgent()
            tutor_in = TutorAgentInput(
                session_id=session_id,
                topic=topic,
                chapter_number=bb.current_chapter,
                prerequisites=["call stack", "synchronous execution"],
                learner_profile=profile,
                previous_misconceptions=profile.current_misconceptions,
                remediation_mode=False,
            )
            materi_md = await tutor.generate_material(tutor_in)
            await artifact_mgr.write_artifact(session_id, "materi.md", materi_md)

            # 3. Generate initial challenges
            assessor = AssessmentAgent()
            challenges = await assessor.generate_challenges(
                materi_text=materi_md,
                profile=profile,
                chapter=bb.current_chapter,
                topic=topic,
            )

            ch_lines = [f"# Chapter {bb.current_chapter} Challenges: {topic}\n"]
            for idx, ch in enumerate(challenges, start=1):
                ch_lines.append(f"## Challenge {idx}: {ch.id} ({ch.type})")
                ch_lines.append(f"**Difficulty:** {ch.difficulty}\n")
                ch_lines.append(f"{ch.prompt}\n")
                if ch.code_snippet:
                    ch_lines.append(f"```javascript\n{ch.code_snippet}\n```\n")

            await artifact_mgr.write_artifact(session_id, "challenge.md", "\n".join(ch_lines))

            save_current_session(session_id)
            console.print(f"[bold green]> Session {session_id} created.[/bold green]")
            console.print(f"[cyan]> materi.md generated for Chapter {bb.current_chapter}.[/cyan]")
            console.print(f"[cyan]> challenge.md written to session directory.[/cyan]")
            console.print(f"[dim]Artifacts located at: {Path(session_dir) / session_id}[/dim]")
        finally:
            await bb_store.close()
            await profile_store.close()

    asyncio.run(_start())


@app.command()
def submit(
    file: Path = typer.Option(..., "--file", "-f", help="Path to submission JavaScript file"),
    session_id: Optional[str] = typer.Option(None, "--session-id", "-s", help="Session ID"),
):
    """Submit code solution for grading and adaptive diagnosis."""
    db_path, session_dir, _ = get_paths()
    sid = get_current_session(session_id)

    if not file.exists():
        console.print(f"[red]Error: Submission file '{file}' not found.[/red]")
        raise typer.Exit(code=1)

    submission_code = file.read_text(encoding="utf-8")

    async def _submit():
        bb_store = BlackboardStore(db_path=db_path)
        profile_store = ProfileStore(db_path=db_path)
        artifact_mgr = ArtifactManager(base_dir=session_dir)
        try:
            bb = await bb_store.read(sid)
            if not bb:
                console.print(f"[red]Session '{sid}' not found in blackboard.[/red]")
                raise typer.Exit(code=1)

            profile = await profile_store.load(bb.learner_id)

            console.print("[cyan]> Running test harness...[/cyan]")
            assessor = AssessmentAgent()
            challenges = await assessor.generate_challenges(
                materi_text="",
                profile=profile,
                chapter=bb.current_chapter,
                topic=bb.current_topic,
            )

            eval_report = await assessor.evaluate_submission(
                session_id=sid,
                chapter=bb.current_chapter,
                topic=bb.current_topic,
                submission_code=submission_code,
                challenges=challenges,
            )

            # Write assessment report
            await artifact_mgr.write_artifact(
                sid, "assessment_report.json", json.dumps(eval_report, indent=2)
            )

            sub_eval = eval_report.get("submission_evaluation", {})
            overall_score = sub_eval.get("overall_score", 0.0)
            pass_fail = sub_eval.get("pass_fail", "fail")
            section_scores = sub_eval.get("section_scores", {})

            await bb_store.update(sid, last_assessment_score=overall_score)

            # Diagnostic update
            diagnostician = DiagnosticAgent()
            diag_input = DiagnosticAgentInput(
                session_id=sid,
                learner_id=bb.learner_id,
                assessment_report=eval_report,
                interaction_log=[],
                current_profile=profile,
            )
            payload, updated_profile = await diagnostician.update_profile(diag_input)

            await artifact_mgr.write_artifact(
                sid, "learner_profile.json", json.dumps(updated_profile.model_dump(), indent=2)
            )
            await profile_store.save(updated_profile)
            await bb_store.update(sid, pending_diagnostic_payload=payload.model_dump())

            console.print(f"[bold]> Overall score: {int(overall_score * 100)}% ({pass_fail.upper()}).[/bold]")
            console.print(f"  - Implementation score: {int(section_scores.get('implementation_correctness', 0) * 100)}%")
            console.print(f"  - Predict output score: {int(section_scores.get('predict_the_output', 0) * 100)}%")

            errors = sub_eval.get("error_taxonomy", [])
            if errors:
                console.print("[yellow]> Error Taxonomy Feedback:[/yellow]")
                for err in errors:
                    console.print(f"  - [{err.get('error_type')}] {err.get('description')}")
                    console.print(f"    Action: {err.get('actionable_feedback')}")

            console.print(f"[dim]> assessment_report.json and learner_profile.json written.[/dim]")
        finally:
            await bb_store.close()
            await profile_store.close()

    asyncio.run(_submit())


@app.command()
def status(
    session_id: Optional[str] = typer.Option(None, "--session-id", "-s", help="Session ID"),
):
    """Display current blackboard state and cognitive profile summary."""
    db_path, _, _ = get_paths()
    sid = get_current_session(session_id)

    async def _status():
        bb_store = BlackboardStore(db_path=db_path)
        profile_store = ProfileStore(db_path=db_path)

        try:
            bb = await bb_store.read(sid)
            if not bb:
                console.print(f"[red]Session '{sid}' not found in blackboard.[/red]")
                raise typer.Exit(code=1)

            profile = await profile_store.load(bb.learner_id)

            table = Table(title=f"AdaptIQ Session Status: {sid}")
            table.add_column("Property", style="bold cyan")
            table.add_column("Value", style="magenta")

            table.add_row("Learner ID", bb.learner_id)
            table.add_row("Topic", bb.current_topic)
            table.add_row("Current Chapter", str(bb.current_chapter))
            table.add_row("Attempt Count", str(bb.attempt_count))
            table.add_row("Last Assessment Score", f"{bb.last_assessment_score}" if bb.last_assessment_score is not None else "None")
            table.add_row("Visual Imagery Score", f"{profile.cognitive_traits.visual_imagery_score}")
            table.add_row("Explanation Modality", profile.cognitive_traits.preferred_explanation_modality)
            table.add_row("Remediation Active", str(bb.remediation_triggered))
            table.add_row("Escalation Flag", str(bb.escalation_flag))

            console.print(table)
        finally:
            await bb_store.close()
            await profile_store.close()

    asyncio.run(_status())


@app.command()
def next(
    session_id: Optional[str] = typer.Option(None, "--session-id", "-s", help="Session ID"),
):
    """Force-advance to the next chapter with updated cognitive adaptation."""
    db_path, session_dir, _ = get_paths()
    sid = get_current_session(session_id)

    async def _next():
        bb_store = BlackboardStore(db_path=db_path)
        profile_store = ProfileStore(db_path=db_path)
        artifact_mgr = ArtifactManager(base_dir=session_dir)

        try:
            bb = await bb_store.read(sid)
            if not bb:
                console.print(f"[red]Session '{sid}' not found.[/red]")
                raise typer.Exit(code=1)

            new_chapter = bb.current_chapter + 1
            await bb_store.update(
                sid,
                current_chapter=new_chapter,
                attempt_count=1,
                remediation_triggered=False,
            )

            profile = await profile_store.load(bb.learner_id)

            # Regenerate materi.md for new chapter reflecting current profile
            tutor = TutorAgent()
            tutor_in = TutorAgentInput(
                session_id=sid,
                topic=bb.current_topic,
                chapter_number=new_chapter,
                prerequisites=["call stack", "synchronous execution"],
                learner_profile=profile,
                previous_misconceptions=profile.current_misconceptions,
                remediation_mode=False,
            )
            materi_md = await tutor.generate_material(tutor_in)
            await artifact_mgr.write_artifact(sid, "materi.md", materi_md)

            # Regenerate challenges
            assessor = AssessmentAgent()
            challenges = await assessor.generate_challenges(
                materi_text=materi_md,
                profile=profile,
                chapter=new_chapter,
                topic=bb.current_topic,
            )
            ch_lines = [f"# Chapter {new_chapter} Challenges: {bb.current_topic}\n"]
            for idx, ch in enumerate(challenges, start=1):
                ch_lines.append(f"## Challenge {idx}: {ch.id} ({ch.type})")
                ch_lines.append(f"**Difficulty:** {ch.difficulty}\n")
                ch_lines.append(f"{ch.prompt}\n")
                if ch.code_snippet:
                    ch_lines.append(f"```javascript\n{ch.code_snippet}\n```\n")

            await artifact_mgr.write_artifact(sid, "challenge.md", "\n".join(ch_lines))

            modality = profile.cognitive_traits.preferred_explanation_modality
            console.print(f"[bold green]> Cognitive profile updated. Explanation mode: {modality}[/bold green]")
            console.print(f"[cyan]> materi.md and challenge.md regenerated for Chapter {new_chapter}.[/cyan]")
        finally:
            await bb_store.close()
            await profile_store.close()

    asyncio.run(_next())


if __name__ == "__main__":
    app()
