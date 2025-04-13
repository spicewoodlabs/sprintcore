import os
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from rich.console import Console
from rich.panel import Panel
import anthropic
import difflib
import re



def generate_prompt(bug_report, file_path, code_chunk, language="JavaScript/Typescript"):
    prompt = f"""
            You are a senior {language} developer.

            Bug Report:
            {bug_report}

            File `{file_path}` contains the following code that may be responsible:
            ```{language}
            {code_chunk}

            Tasks:
            1. Identify the bug
            2. Suggest fix along with the line number that needs to be fixed
            3. Provide a summary of what needs to be fixed
            4. Respond with:
            Bug identification:
            <Bug identification here>
            -------------
            Suggested fix:
            <suggested fix here>
            -------------
            Summary of the fix:
            <summar of the fix here>
            -------------
            Original code:
            <original code here>
            --------------
            Fixed Code:
            <your fixed version here>
            
            
            """
    return prompt
def print_claude_raw_response(response):
    console = Console()
    
    console.print(Panel.fit(response, title="✅ Claude suggested fix: ", border_style="green"))
    
    
def ask_claude_to_fix_nextjs_bug(bug_report, file_path, code_chunk, stream_resp, language="JavaScript/Typescript"):
    
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    prompt = generate_prompt(bug_report,file_path,code_chunk)
    claude_model = "claude-3-7-sonnet-20250219"
    print(f"using claude_model = {claude_model}")
    response_text = ""
    if (stream_resp == "False"):
        
        response = client.messages.create( model=claude_model, max_tokens=1500, temperature=0.3, messages=[{"role": "user", "content": prompt}] ) 
        response_text = response.content[0].text
    else: 
        
        with client.messages.stream(
            model=claude_model,  # or claude-3-sonnet / claude-3-haiku
            max_tokens=1024,
            temperature=0.7,
            messages=[
                {"role": "user", "content": prompt}
            ],
        ) as stream:
            for text in stream.text_stream:
                print(text, end="", flush=True)
                response_text = response_text + text
    return response_text

def  fix_code_with_claude_and_print_diff(results, query_text, k, stream_resp=False):
    
    for i, doc in enumerate(results):
        meta = doc.metadata
        code = doc.page_content
        file_path = meta.get("source", "unknown")
        name = meta.get("name", "")
        start_line = meta.get("start_line", 0)

        # Ask Claude to fix it
        print(f"\n🤖 Sending top result to Claude for bug fix suggestion...\n")
        
        claude_response = ask_claude_to_fix_nextjs_bug(query_text, file_path, code,  stream_resp)
        console = Console()
        
        console.print(Panel.fit(claude_response, title="✅ Bug Fix", border_style="green"))

        # Extract the code block from Claude's response
        #match = re.search(r"```(?:\w+)?\n(.+?)```", claude_response, re.DOTALL)
        #fixed_code = match.group(1).strip() if match else ""

        # Generate diff
        #original_lines = code.splitlines()
        #fixed_lines = fixed_code.splitlines()

        #diff = difflib.unified_diff(
        #    original_lines, fixed_lines,
        #    fromfile="original", tofile="fixed",
        #    fromfiledate=f"{file_path}:{start_line}",
        #    tofiledate="ClaudeFix",
        #    lineterm=""
        #)
        

        #console.print("\n📊 Diff (with line numbers):\n", style="bold yellow")
        #console.print("\n".join(diff), style="blue")
        break  # only top result


def print_topk_matching_files(results, query_text, k):
    console = Console()
    console.print(f"\n🔍 Top {k} results for:\n[bold yellow]\"{query_text}\"[/bold yellow]\n")
    for i, doc in enumerate(results):
        
        metadata = doc.metadata
        source_file = metadata["source"]
        code = doc.page_content
        file_name = os.path.basename(source_file)

        header = f"[{i+1}] 📄 {file_name} (lines {metadata.get('start_line')}–{metadata.get('end_line')})"
        if metadata.get("name"):
            header += f" | 🔧 Function: [cyan]{metadata['name']}[/cyan]"
        
        console.print(Panel.fit(code, title=header, border_style="blue"))
        

def load_index(index_dir="index"):
    
    embeddings = OpenAIEmbeddings()
    return FAISS.load_local(index_dir, embeddings, allow_dangerous_deserialization=True)

def fix_bug(args):
    index_dir="index"
    print("fix_bug")
    bug_description = args.bug_description
    query_text = bug_description
    mode=args.mode
    top_k = args.top_k
    stream_resp = args.stream_resp
    
    db = load_index(index_dir)
    
    results = db.similarity_search(query_text, k=top_k)

    
    print(f"top {top_k} matches")
    print_topk_matching_files(results,query_text,top_k)

    if (mode == "fix_code"):
        console = Console()
        
        with console.status("Going to fix the code now...\n", spinner="material"):
            fix_code_with_claude_and_print_diff(results,query_text,top_k, stream_resp)

    
