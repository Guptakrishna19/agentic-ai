# Week 5 · Day 2: RAG — Document Loading & Chunking

**Intern:** Dhruv Lukhi  
**Day:** Day 22  
**Level:** Beginner → Intermediate

---

## Learn First (Complete Before Tasks)

Study these topics **before** you start today's tasks. Take notes in `learn-first-notes.md`.

1. Document loaders in LangChain: PDF, TXT, web pages
2. Why chunk documents? LLMs have limited context window
3. Chunking strategies: fixed size, by paragraph, by sentence
4. What is chunk overlap and why it helps

---

## Today's Tasks

Complete these in order. Do not skip ahead — each step builds on the previous one.

### Step 1
Create 3 sample text files (or download 2 PDFs) about a topic you know

### Step 2
Use LangChain document loaders to load your files

### Step 3
Try 2 chunking strategies: `CharacterTextSplitter` (500 chars) and `RecursiveCharacterTextSplitter`

### Step 4
Print chunk count and first chunk from each strategy. Compare in `chunking-comparison.md`

---

## Deliverable

`load_and_chunk.py` + sample documents + `chunking-comparison.md`

Save all files in this folder (`day-22/`).

---

## Recommended Resources

- LangChain Document Loaders: https://python.langchain.com/docs/concepts/document_loaders/
- Text Splitters: https://python.langchain.com/docs/concepts/text_splitters/

---

## Stretch Goal (Optional — if you finish early)

Chunk a PDF and visualize chunk sizes with a bar chart

---

## Completion Checklist

- [ ] Completed all "Learn First" topics and wrote notes
- [ ] Finished all task steps
- [ ] Saved deliverable in this folder
- [ ] Wrote 3 things I learned today in `reflection.md`
- [ ] Wrote 1 doubt/blocker (if any) to ask mentor

