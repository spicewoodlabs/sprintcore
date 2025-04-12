
import os
import re
from langchain.docstore.document import Document
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from pathlib import Path
from tree_sitter import Parser, Language
import tree_sitter_javascript as ts_js        # .js / .jsx
import tree_sitter_typescript  as ts_ts # for .tsx files
JS_LANGUAGE = Language(ts_js.language())

TS_LANGUAGE = Language(ts_ts.language_typescript())

def extract_chunks_from_tsx_js(tree, code, max_tok=800):
    
    """Return semantically‑clean chunks (top‑level declarations) and
       fall back to token‑based slices so each ≤ max_tok."""
    src = code.decode()
    
    chunks_with_lines = [
        {
            "code": src[n.start_byte:n.end_byte],
            "start_line": n.start_point[0] + 1,  # converting to 1-based line number
            "end_line": n.end_point[0] + 1
        }
        #src[n.start_byte:n.end_byte]
        for n in tree.root_node.children
        
        if n.type in {
            "function_declaration","lexical_declaration",
            "class_declaration","export_statement"
        }
    ]
    
    # coarse slice for anything still too big
    return chunks_with_lines

def parse_file(path: Path):

    if path.suffix=='.tsx': 
        parser = Parser(TS_LANGUAGE); 
    else:
        parser = Parser(JS_LANGUAGE); 
    
    code   = path.read_bytes()
    
    return parser.parse(code), code

def index_code(args):
    source_dir = args.source_code
    print(f"source_dir={source_dir}")
    index_dir = args.index
    docs = []
    for root, _, files in os.walk(source_dir):
        for file in files:
           
           if file.endswith((".js", ".jsx", ".ts", ".tsx","css")):
                path = os.path.join(root, file)
                print(f"indexing file... {path}")
                
                #chunks = chunk_nextjs_file(path)
                tree, code = parse_file(Path(path))

                chunks = extract_chunks_from_tsx_js(tree,code)
               
                for chunk in chunks:
                    
                    doc = Document(
                        page_content=chunk["code"],
                        metadata={
                            "source": path,
                            "start_line": chunk["start_line"],
                            "end_line": chunk["end_line"]
                        }
                    )
                    docs.append(doc)

    
    

    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embeddings)
    db.save_local(index_dir)
    print(f"Successfully created the code index")