import argparse
import os
import sys
from dotenv import load_dotenv, find_dotenv

from sprintcore.cli.prd2story import prd2story

def main():
    env_path = find_dotenv()
    load_dotenv(dotenv_path=env_path, override=True)
    print(f"🔍 Loaded environment variables from: {env_path if env_path else 'None'}")

    for var in ["OPENAI_API_KEY", "JIRA_URL", "JIRA_USER", "JIRA_PROJECT"]:
        val = os.getenv(var)
        from_env = env_path and var in open(os.path.expanduser(env_path)).read()
        source = ".env" if from_env else "shell"
        if not from_env:
            print(f"❌ {var} must be set in the .env file, but was loaded from the shell.")
            sys.exit(1)

    parser = argparse.ArgumentParser(prog='sprintcore', description='SprintCore CLI - AI-powered sprint planning')
    subparsers = parser.add_subparsers(dest='command', required=True)

    prd_parser = subparsers.add_parser('create-story', help='Convert PRD to structured user stories')
    prd_parser.add_argument('--input', '-i', required=True, help='Input .md file')
    prd_parser.add_argument('--prompt', '-p', default='prompt.txt', help='Prompt template file')
    prd_parser.add_argument('--output', '-o', help='Output file (.json/.yaml/.md)')
    prd_parser.add_argument('--model', default='gpt-4', help='OpenAI model')
    prd_parser.add_argument('--mock', action='store_true', help='Use mock response instead of OpenAI API')
    prd_parser.add_argument('--use-jira', action='store_true', help='Create stories and subtasks in Jira')
    prd_parser.set_defaults(func=prd2story)

    args = parser.parse_args()
    result = args.func(args)
 
if __name__ == '__main__':
    main()
