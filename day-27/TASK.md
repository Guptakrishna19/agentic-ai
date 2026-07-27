# Week 6 · Day 2: LangGraph — Multi-Step RAG Workflow

**Intern:** Dhruv Lukhi  
**Day:** Day 27  
**Level:** Intermediate

---

## Learn First (Complete Before Tasks)

Study these topics **before** you start today's tasks. Take notes in `learn-first-notes.md`.

1. Conditional edges: route to different nodes based on output
2. Example: if question is about docs → RAG node; if general → direct LLM node
3. State schema design: what data each node needs
4. Debugging graphs: printing state at each step

---

## Today's Tasks

Complete these in order. Do not skip ahead — each step builds on the previous one.

### Step 1
Build a LangGraph with 3 nodes: classify_question → retrieve_docs → generate_answer

### Step 2
Add conditional routing: factual questions go to RAG, chitchat goes to direct LLM

### Step 3
Test with 8 questions (4 factual, 4 chitchat). Log which path each took

### Step 4
Save execution traces in `graph-traces.md`

---

## Deliverable

`rag_graph.py` + `graph-traces.md`

Save all files in this folder (`day-27/`).

---

## Recommended Resources

- LangGraph conditional edges: https://langchain-ai.github.io/langgraph/how-tos/graph-api/
- RAG + LangGraph example: https://langchain-ai.github.io/langgraph/tutorials/rag/

---

## Stretch Goal (Optional — if you finish early)

Add a "clarify" node that asks user to rephrase vague questions

---

## Completion Checklist

- [ ] Completed all "Learn First" topics and wrote notes
- [ ] Finished all task steps
- [ ] Saved deliverable in this folder
- [ ] Wrote 3 things I learned today in `reflection.md`
- [ ] Wrote 1 doubt/blocker (if any) to ask mentor

