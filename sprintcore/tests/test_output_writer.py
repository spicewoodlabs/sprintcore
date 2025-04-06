from core.output_writer import write_output
import os

def test_write_output_json(tmp_path):
    path = tmp_path / "sprint.json"
    data = [{
        "epic_name": "Test Epic",
        "description": "Test Desc",
        "stories": [{"story_name": "Story", "acceptance_criteria": "", "subtasks": ["a"]}]
    }]
    write_output(data, str(path))
    assert path.read_text().startswith('[')

def test_write_output_md(tmp_path):
    path = tmp_path / "sprint.md"
    data = [{
        "epic_name": "Epic",
        "description": "Desc",
        "stories": [{"story_name": "S", "acceptance_criteria": "", "subtasks": ["t1"]}]
    }]
    write_output(data, str(path))
    assert "## Epic" in path.read_text()
