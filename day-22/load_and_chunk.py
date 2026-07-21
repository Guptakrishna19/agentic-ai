import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
)

# --------------------------------------------------
# STEP 2: Load the text files
# --------------------------------------------------

# Determine absolute path to the documents directory based on script location
script_dir = os.path.dirname(os.path.abspath(__file__))
file_paths = [
    os.path.join(script_dir, "documents", "artificial-intelligence.txt"),
    os.path.join(script_dir, "documents", "machine-learning.txt"),
    os.path.join(script_dir, "documents", "generative-ai.txt"),
]

documents = []

for file_path in file_paths:
    loader = TextLoader(file_path, encoding="utf-8")
    loaded_docs = loader.load()
    documents.extend(loaded_docs)

print(f"Total documents loaded: {len(documents)}")


# --------------------------------------------------
# STEP 3A: CharacterTextSplitter
# --------------------------------------------------

character_splitter = CharacterTextSplitter(
    separator="",
    chunk_size=500,
    chunk_overlap=50,
)

character_chunks = character_splitter.split_documents(documents)

print("\n========== CharacterTextSplitter ==========")
print(f"Chunk count: {len(character_chunks)}")

if character_chunks:
    print("\nFirst chunk:")
    print(character_chunks[0].page_content)


# --------------------------------------------------
# STEP 3B: RecursiveCharacterTextSplitter
# --------------------------------------------------

recursive_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
)

recursive_chunks = recursive_splitter.split_documents(documents)

print("\n========== RecursiveCharacterTextSplitter ==========")
print(f"Chunk count: {len(recursive_chunks)}")

if recursive_chunks:
    print("\nFirst chunk:")
    print(recursive_chunks[0].page_content)


# --------------------------------------------------
# STEP 4: Generate comparison Markdown file
# --------------------------------------------------

character_first_chunk = (
    character_chunks[0].page_content
    if character_chunks
    else "No chunks generated."
)

recursive_first_chunk = (
    recursive_chunks[0].page_content
    if recursive_chunks
    else "No chunks generated."
)

comparison = f"""# Chunking Strategy Comparison

## Documents Used

Three sample text documents were used:

1. Artificial Intelligence
2. Machine Learning
3. Generative AI

Total documents loaded: {len(documents)}

---

## Strategy 1: CharacterTextSplitter

### Configuration

- Chunk size: 500 characters
- Chunk overlap: 50 characters

### Chunk Count

{len(character_chunks)}

### First Chunk

```text
{character_first_chunk}
```

---

## Strategy 2: RecursiveCharacterTextSplitter

### Configuration

- Chunk size: 500 characters
- Chunk overlap: 50 characters

### Chunk Count

{len(recursive_chunks)}

### First Chunk

```text
{recursive_first_chunk}
```
"""

# Write comparison to chunking-comparison.md in the script's directory
output_file = os.path.join(script_dir, "chunking-comparison.md")
with open(output_file, "w", encoding="utf-8") as f:
    f.write(comparison)

print(f"\nSuccessfully generated comparison file at: {output_file}")