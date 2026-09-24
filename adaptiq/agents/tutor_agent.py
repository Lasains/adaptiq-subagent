"""Tutor Agent for generating adaptive learning materials (materi.md)."""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional
from pydantic import BaseModel, Field

from adaptiq.state.learner_profile import LearnerProfile


class TutorAgentInput(BaseModel):
    session_id: str
    topic: str
    chapter_number: int = 1
    prerequisites: list[str] = Field(default_factory=list)
    learner_profile: LearnerProfile
    previous_misconceptions: list[str] = Field(default_factory=list)
    remediation_mode: bool = False


class TutorAgent:
    """Pedagogical Tutor Agent responsible for generating materi.md."""

    def __init__(
        self,
        prompt_template_path: Optional[str] = None,
        api_key: Optional[str] = None,
    ):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.template_path = Path(
            prompt_template_path
            or Path(__file__).parent.parent / "prompts" / "tutor_system_prompt.txt"
        )

    def determine_modality(self, visual_imagery_score: float) -> str:
        if visual_imagery_score <= 3.0:
            return "aphantasia_adapted"
        elif visual_imagery_score >= 8.0:
            return "hyper_visual"
        return "standard"

    async def generate_material(self, agent_input: TutorAgentInput) -> str:
        score = agent_input.learner_profile.cognitive_traits.visual_imagery_score
        modality = self.determine_modality(score)

        # Attempt live LLM call if api_key is configured
        if self.api_key and not self.api_key.startswith("your_"):
            try:
                from google import genai

                client = genai.Client(api_key=self.api_key)
                prompt_template = self.template_path.read_text(encoding="utf-8")

                system_prompt = (
                    prompt_template.replace("{{session_id}}", agent_input.session_id)
                    .replace("{{topic}}", agent_input.topic)
                    .replace("{{chapter_number}}", str(agent_input.chapter_number))
                    .replace("{{remediation_mode}}", str(agent_input.remediation_mode).lower())
                    .replace("{{prerequisites}}", json.dumps(agent_input.prerequisites))
                    .replace(
                        "{{learner_profile_json}}",
                        json.dumps(agent_input.learner_profile.model_dump(), indent=2),
                    )
                    .replace(
                        "{{previous_misconceptions_array}}",
                        json.dumps(agent_input.previous_misconceptions),
                    )
                )

                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents="Generate materi.md according to system instructions.",
                    config={
                        "system_instruction": system_prompt,
                        "temperature": 0.7,
                        "max_output_tokens": 4096,
                    },
                )
                if response.text and response.text.strip():
                    return response.text.strip()
            except Exception as e:
                # Log and fallback to offline generator
                print(f"[TutorAgent] Warning: LLM generation error ({e}), falling back to deterministic template.")

        # High-fidelity deterministic fallback matching PRD Section 3.1
        return self._generate_fallback_material(agent_input, modality, score)

    def _generate_fallback_material(
        self, agent_input: TutorAgentInput, modality: str, score: float
    ) -> str:
        now_iso = datetime.now(timezone.utc).isoformat()
        is_aphantasia = modality == "aphantasia_adapted"

        if is_aphantasia:
            mechanism_section = """## 2. Core Mechanism (State Machine & Trace)

The runtime maintains five distinct operational phases:
1. `EXEC_STACK`: Synchronous frame evaluation
2. `CHECK_MICROTASK`: Evaluates and empties microtask queue
3. `RENDER_CHECK`: Browser paint opportunity
4. `DEQUEUE_MACROTASK`: Shift single macrotask into execution stack
5. `LOOP_RECYCLE`: Return to Step 1

```
State Transition Table:
[RUNNING] ---> [STACK_EMPTY] ---> [DRAIN_MICROTASK] ---> [DRAIN_MACROTASK] ---> [IDLE]
```"""
            trace_section = """## 4. Execution Trace Table (Aphantasia-Adapted)

| Step | Call Stack State     | Web API Queue   | Microtask Queue | Macrotask Queue | Console Output |
|------|----------------------|-----------------|-----------------|-----------------|----------------|
| 1    | [main()]             | -               | -               | -               | -              |
| 2    | [main(), log('A')]   | -               | -               | -               | A              |
| 3    | [main(), setTimeout] | timer(cb1, 0ms) | -               | -               | -              |
| 4    | [main(), Promise]    | -               | [cb_micro]      | -               | -              |
| 5    | [main(), log('D')]   | -               | [cb_micro]      | [cb_macro]      | D              |
| 6    | [EMPTY]              | -               | []              | [cb_macro]      | C              |
| 7    | [cb_macro]           | -               | []              | []              | B              |"""
        else:
            mechanism_section = """## 2. Core Mechanism

The Event Loop continuously coordinates synchronous execution with background task queues.

**Analogy:** Think of the runtime like a single chef (Call Stack) preparing meals. When an order takes time to bake (setTimeout/fetch), the chef places it in an oven (Web API) and continues with the next immediate dish. When the timer rings, the ready dish is moved to a serving counter (Queue) until the chef's hands are free."""
            trace_section = """## 4. Execution Trace Table

| Step | Call Stack State     | Web API Queue   | Microtask Queue | Macrotask Queue | Console Output |
|------|----------------------|-----------------|-----------------|-----------------|----------------|
| 1    | [main()]             | -               | -               | -               | -              |
| 2    | [main(), log('A')]   | -               | -               | -               | A              |
| 3    | [main(), setTimeout] | timer(cb1, 0ms) | -               | -               | -              |
| 4    | [main(), log('D')]   | -               | -               | [cb_macro]      | D              |
| 5    | [cb_macro]           | -               | -               | []              | B              |"""

        return f"""---
artifact_type: "materi"
session_id: "{agent_input.session_id}"
topic: "{agent_input.topic}"
chapter: {agent_input.chapter_number}
estimated_reading_time_minutes: 10
prerequisites: {json.dumps(agent_input.prerequisites)}
cognitive_profile_applied: "{modality}"
visual_imagery_score_at_generation: {score}
remediation_mode: {str(agent_input.remediation_mode).lower()}
chapter_overflow: false
generated_at: "{now_iso}"
misconceptions_targeted: {json.dumps(agent_input.previous_misconceptions)}
---

# Chapter {agent_input.chapter_number}: {agent_input.topic}

## 1. Formal Definition
The JavaScript Event Loop is a single-threaded concurrent execution coordinator that processes frames sequentially from the Call Stack and enqueues asynchronous callbacks across microtask and macrotask FIFO queues.

{mechanism_section}

## 3. Annotated Code Specimen
```javascript
console.log('A');           // STACK: [main]            -> PRINT: A
setTimeout(() => {{
  console.log('B');         // MACROTASK: executed after microtask drain
}}, 0);
Promise.resolve().then(() => {{
  console.log('C');         // MICROTASK: priority queue drained immediately after stack
}});
console.log('D');           // STACK: [main]            -> PRINT: D
```

{trace_section}

## 5. Misconception Inoculation
- **Misconception:** `setTimeout(fn, 0)` executes synchronously or immediately on the next line.
- **Correction:** `setTimeout` delegates to host timers (Web API / libuv). Its callback enters the Macrotask Queue and runs only after the Call Stack and Microtask Queue are completely clear.

## 6. Concept Check (Pre-Assessment Primer)
1. Which queue has absolute priority when the Call Stack becomes empty: Microtasks or Macrotasks?
2. What is the output order of lines A, B, C, and D in Section 3?
"""
