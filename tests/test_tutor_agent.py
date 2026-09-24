"""Tests for TutorAgent, CodeValidator, and materi.md generation."""

import re
import pytest
import yaml

from adaptiq.agents.tutor_agent import TutorAgent, TutorAgentInput, FORBIDDEN_APHANTASIA_WORDS
from adaptiq.state.learner_profile import LearnerProfile, DEFAULT_PROFILE
from adaptiq.tools.code_validator import CodeValidator
from adaptiq.tools.sandbox_executor import SandboxExecutor


@pytest.fixture
def tutor_agent():
    return TutorAgent()


@pytest.fixture
def default_input():
    return TutorAgentInput(
        session_id="sess_test_001",
        topic="JavaScript Closures",
        chapter_number=1,
        prerequisites=["scope", "functions"],
        learner_profile=DEFAULT_PROFILE,
        previous_misconceptions=[],
        remediation_mode=False,
    )


def test_modality_switch(tutor_agent):
    assert tutor_agent.determine_modality(1.0) == "aphantasia_adapted"
    assert tutor_agent.determine_modality(3.0) == "aphantasia_adapted"
    assert tutor_agent.determine_modality(3.1) == "standard"
    assert tutor_agent.determine_modality(5.0) == "standard"
    assert tutor_agent.determine_modality(7.9) == "standard"
    assert tutor_agent.determine_modality(8.0) == "hyper_visual"
    assert tutor_agent.determine_modality(10.0) == "hyper_visual"


@pytest.mark.asyncio
async def test_aphantasia_mode_forbidden_words_and_enforcement(tutor_agent, default_input):
    profile = default_input.learner_profile.model_copy(deep=True)
    profile.cognitive_traits.visual_imagery_score = 2.0
    agent_input = default_input.model_copy(update={"learner_profile": profile})

    content = await tutor_agent.generate_material(agent_input)

    # Check forbidden words: case-insensitive
    lower_content = content.lower()
    for word in FORBIDDEN_APHANTASIA_WORDS:
        assert word.lower() not in lower_content, f"Forbidden word '{word}' found in aphantasia content"

    # Enforce trace table + state machine
    assert "trace table" in lower_content or "| step |" in lower_content
    assert "state machine" in lower_content or "state transition" in lower_content


@pytest.mark.asyncio
async def test_yaml_frontmatter_validity(tutor_agent, default_input):
    content = await tutor_agent.generate_material(default_input)

    # Must start with --- and have a closing ---
    match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    assert match is not None, "materi.md does not contain valid YAML frontmatter delimiters"

    yaml_block = match.group(1)
    meta = yaml.safe_load(yaml_block)

    assert isinstance(meta, dict)
    assert meta.get("artifact_type") == "materi"
    assert meta.get("session_id") == default_input.session_id
    assert meta.get("topic") == default_input.topic
    assert meta.get("chapter") == default_input.chapter_number
    assert "estimated_reading_time_minutes" in meta
    assert meta.get("cognitive_profile_applied") in ["standard", "aphantasia_adapted", "hyper_visual"]
    assert "visual_imagery_score_at_generation" in meta


@pytest.mark.asyncio
async def test_code_validator_extract_and_success():
    validator = CodeValidator()
    md_content = """# Sample Material
```javascript
const a = 10;
const b = 20;
console.log(a + b);
```
Some middle text.
```js
function add(x, y) {
  return x + y;
}
console.log(add(1, 2));
```
"""
    snippets = validator.extract_code_blocks(md_content)
    assert len(snippets) == 2

    is_valid, errors = await validator.validate_markdown(md_content)
    assert is_valid is True
    assert len(errors) == 0


@pytest.mark.asyncio
async def test_code_validator_error_detection():
    validator = CodeValidator()
    broken_md = """# Broken Material
```javascript
const x = ; // syntax error
```
"""
    is_valid, errors = await validator.validate_markdown(broken_md)
    assert is_valid is False
    assert len(errors) == 1
    assert "SyntaxError" in errors[0] or "error" in errors[0].lower()


@pytest.mark.asyncio
async def test_tutor_agent_generated_material_passes_validator(tutor_agent, default_input):
    validator = CodeValidator()
    content = await tutor_agent.generate_material(default_input)
    is_valid, errors = await validator.validate_markdown(content)
    assert is_valid is True, f"Code snippets in generated materi.md failed validation: {errors}"
