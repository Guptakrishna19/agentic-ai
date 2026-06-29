# Week 3 · Day 2: Build Your First API with FastAPI

**Intern:** Dhruv Lukhi  
**Day:** Day 12  
**Level:** Beginner → Intermediate

---

## Learn First (Complete Before Tasks)

Study these topics **before** you start today's tasks. Take notes in `learn-first-notes.md`.

1. What is FastAPI? Why Python developers use it
2. Routes, path parameters, query parameters
3. How to return JSON from an API
4. Auto-generated API docs at `/docs`

---

## Today's Tasks

Complete these in order. Do not skip ahead — each step builds on the previous one.

### Step 1
Install FastAPI and uvicorn: `pip install fastapi uvicorn`

### Step 2
Create `main.py` with 3 endpoints: GET `/hello`, GET `/items/{item_id}`, POST `/items`

### Step 3
Run server: `uvicorn main:app --reload`. Test all endpoints in browser and Postman

### Step 4
Add Pydantic model for request body validation on POST endpoint

---

## Deliverable

`main.py` + screenshots of `/docs` page and API responses

Save all files in this folder (`day-12/`).

---

## Recommended Resources

- FastAPI tutorial: https://fastapi.tiangolo.com/tutorial/
- First steps video: https://www.youtube.com/watch?v=tLKKmouUams

---

## Stretch Goal (Optional — if you finish early)

Add a GET endpoint that returns a list of items with pagination

---

## Completion Checklist

- [ ] Completed all "Learn First" topics and wrote notes
- [ ] Finished all task steps
- [ ] Saved deliverable in this folder
- [ ] Wrote 3 things I learned today in `reflection.md`
- [ ] Wrote 1 doubt/blocker (if any) to ask mentor

