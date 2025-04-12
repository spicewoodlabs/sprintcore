import argparse
import os
import sys
from dotenv import load_dotenv, find_dotenv

from sprintcore.cli.prd2story import prd2story
from sprintcore.cli.doc_embeddings import index_code
from sprintcore.cli.fix_bugs_agent import fix_bug

def main():
    env_path = find_dotenv()
    load_dotenv(dotenv_path=env_path, override=True)
    
    for var in ["OPENAI_API_KEY", "ANTHROPIC_API_KEY"]:
        val = os.getenv(var)
        
        from_env = env_path and var in open(os.path.expanduser(env_path)).read()
        source = ".env" if from_env else "shell"
        if not from_env:
            print(f"❌ {var} must be set in the .env file, but was loaded from the shell.")
            sys.exit(1)

    parser = argparse.ArgumentParser(prog='sprintcore', description='SprintCore CLI - AI-powered sprint planning')
    subparsers = parser.add_subparsers(dest='command', required=True)

    prd_parser = subparsers.add_parser('create-story', help='Convert PRD to structured user stories')
    prd_parser.add_argument('--input', required=True, help='Input .md file')
    prd_parser.add_argument('--prompt', default='prompt.txt', help='Prompt template file')
    prd_parser.add_argument('--output', help='Output file (.json/.yaml/.md)')
    prd_parser.add_argument('--model', default='gpt-4', help='OpenAI model')
    prd_parser.add_argument('--mock', action='store_true', help='Use mock response instead of OpenAI API')
    prd_parser.add_argument('--use_jira', action='store_true', help='Create stories and subtasks in Jira')
    prd_parser.set_defaults(func=prd2story)

    index_code_parser = subparsers.add_parser('index-code', help='Index your code base for bug fixing')
    index_code_parser.add_argument('--lang ', default='nextjs', help='nextjs, javascript (java coming soon)')
    index_code_parser.add_argument('--source_code', required=True, help='Source code directory to index')
    index_code_parser.add_argument('--index',  default='index', help='Name of the index (optional)')

    query_index_parser = subparsers.add_parser('bug-fix', help='Find top k files that matches the bug descriptiion')
    query_index_parser.add_argument('--bug_description', required=True, help='Description of the bug')
    query_index_parser.add_argument('--top_k', default=3, help='Top k similar matches')
    query_index_parser.add_argument('--mode', default='query', help='query to query the index; fix_code for fixing code')
   
    
   
    prd_parser.set_defaults(func=prd2story)
    index_code_parser.set_defaults(func=index_code)
    query_index_parser.set_defaults(func=fix_bug)

    args = parser.parse_args()
    result = args.func(args)
 
if __name__ == '__main__':
    main()
