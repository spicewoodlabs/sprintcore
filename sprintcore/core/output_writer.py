import json
import yaml

def write_output(data, output_path):
    print("creating the output file...")
    ext = output_path.split('.')[-1]
    with open(output_path, 'w', encoding='utf-8') as f:
        if ext == 'json':
            json.dump(data, f, indent=2)
        elif ext in ('yaml', 'yml'):
            yaml.dump(data, f, sort_keys=False)
        elif ext == 'md':
            for epic in data:
                f.write(f"## Epic: {epic['epic_name']}\n{epic['description']}\n\n")
                for story in epic['stories']:
                    f.write(f"### Story: {story['story_name']}\n")
                    if 'acceptance_criteria' in story:
                        f.write(f"- *Acceptance Criteria:* {story['acceptance_criteria']}\n")
                    for subtask in story['subtasks']:
                        f.write(f"  - [ ] {subtask}\n")
                f.write("\n")
        else:
            raise ValueError("Unsupported file format: " + ext)
