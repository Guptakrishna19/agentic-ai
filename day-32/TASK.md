# Week 7 · Day 2: Caching & Performance for AI Apps

**Intern:** Dhruv Lukhi  
**Day:** Day 32  
**Level:** Beginner → Intermediate

---

## Learn First (Complete Before Tasks)

Study these topics **before** you start today's tasks. Take notes in `learn-first-notes.md`.

1. What is caching? Store frequent results to avoid recomputing
2. Redis basics: in-memory key-value store
3. What to cache in AI apps: embeddings, frequent queries, LLM responses
4. TTL (Time To Live): when cached data expires

---

## Today's Tasks

Complete these in order. Do not skip ahead — each step builds on the previous one.

### Step 1
Install Redis locally (or use Redis Docker image)

### Step 2
Add caching to your RAG app: cache embedding results for same document

### Step 3
Add query cache: if same question asked twice, return cached answer

### Step 4
Measure response time with and without cache. Document in `cache-benchmark.md`

---

## Deliverable

Updated RAG app with caching + `cache-benchmark.md`

Save all files in this folder (`day-32/`).

---

## Recommended Resources

- Redis crash course: https://www.youtube.com/watch?v=G1rOthIU-uo
- Python redis library: https://redis-py.readthedocs.io/

---

## Stretch Goal (Optional — if you finish early)

Add cache invalidation when a new document is uploaded

---

## Completion Checklist

- [ ] Completed all "Learn First" topics and wrote notes
- [ ] Finished all task steps
- [ ] Saved deliverable in this folder
- [ ] Wrote 3 things I learned today in `reflection.md`
- [ ] Wrote 1 doubt/blocker (if any) to ask mentor

