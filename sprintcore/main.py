import argparse
import os
import sys
from dotenv import load_dotenv, find_dotenv

from sprintcore.cli.prd2story import prd2story
from sprintcore.cli.doc_embeddings import index_code
from sprintcore.cli.fix_bugs_agent import fix_bug

def main():
    env_path = find_dotenv()
    
    load_dotenv(dotenv_path='.env', override=True)
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
    
    required_keys = ["OPENAI_API_KEY", "ANTHROPIC_API_KEY"]
    missing_key = 0
    for key in required_keys:
        if not os.getenv(key):
            missing_key = 1
            print(f"❌ {key} is missing")
        else:
            print(f"✅ {key} is loaded")

    if (missing_key == 1): 
        print("❌ One or more API keys are missing!")
        print("You can copy .env.example to .env. API keys should be set in .env")
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
    query_index_parser.add_argument('--stream_resp', default='False', help='stream the response')
   
    
   
    prd_parser.set_defaults(func=prd2story)
    index_code_parser.set_defaults(func=index_code)
    query_index_parser.set_defaults(func=fix_bug)

    args = parser.parse_args()
    result = args.func(args)
 
if __name__ == '__main__':
    main()
