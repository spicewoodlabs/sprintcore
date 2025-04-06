import os
from sprintcore.core.parser import parse_prd
from sprintcore.core.output_writer import write_output

def prd2story(args):
    # Load input markdown
    print("reading the PRD...")
    with open(args.input, 'r', encoding='utf-8') as f:
        requirements_md = f.read()

    # Load prompt template
    print("reading the prompt...")
    with open(args.prompt, 'r', encoding='utf-8') as f:
        prompt_template = f.read()

    # Use parser module to process
    data = parse_prd(requirements_md, prompt_template, model=args.model, mock=args.mock)

    # Write output
    if args.output:
        write_output(data, args.output)
        print(f"✅ Output saved to {args.output}")
