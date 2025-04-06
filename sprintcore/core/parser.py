import os
import json
from openai import OpenAI

def parse_prd(requirements_md: str, prompt_template: str, model: str, mock: bool = False):
    prompt = prompt_template.replace('{{REQUIREMENTS}}', requirements_md)

    if mock:
        print("⚙️ Using mock response")
        return [
            {
                "epic_name": "Mock Epic",
                "description": "This is a mock epic description.",
                "stories": [
                    {
                        "story_name": "Mock story",
                        "acceptance_criteria": "It should work as a mock",
                        "subtasks": ["Subtask 1", "Subtask 2"]
                    }
                ]
            }
        ]

    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("Missing OPENAI_API_KEY")

    client = OpenAI(api_key=api_key)

    print("thinking & reasoning...")
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a senior product manager who writes structured specs."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4,
        stream=True
    )
    full_response = ""
    for chunk in response:
        content = chunk.choices[0].delta.content
        if content:
            print(content, end="", flush=True)
            full_response += content

    
    if full_response.startswith("```json"):
        content = full_response.replace("```json", "").replace("```", "").strip()

    return json.loads(full_response)
