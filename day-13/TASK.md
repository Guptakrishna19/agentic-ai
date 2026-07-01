# Week 3 · Day 3: Connect API to Database

**Intern:** Dhruv Lukhi  
**Day:** Day 13  
**Level:** Intermediate

---

## Learn First (Complete Before Tasks)

Study these topics **before** you start today's tasks. Take notes in `learn-first-notes.md`.

1. How backend apps connect to databases (connection string, cursor)
2. CRUD API pattern: one endpoint per operation
3. Why we use environment variables for secrets (not hardcoded passwords)
4. What is `.env` file and `python-dotenv`

---

## Today's Tasks

Complete these in order. Do not skip ahead — each step builds on the previous one.

### Step 1
Connect your FastAPI app to `intern.db` from Week 2

### Step 2
Create CRUD endpoints for employees: GET all, GET by id, POST new, PUT update, DELETE

### Step 3
Test every endpoint with Postman. Save requests as a Postman collection

### Step 4
Move database path to a `.env` file. Add `.env` to `.gitignore`

---

## Deliverable

`api/` folder with FastAPI app + Postman collection export + `.env.example`

Save all files in this folder (`day-13/`).

---

## Recommended Resources

- FastAPI + SQL: https://fastapi.tiangolo.com/tutorial/sql-databases/
- python-dotenv: https://pypi.org/project/python-dotenv/

---

## Stretch Goal (Optional — if you finish early)

Add input validation: salary must be positive, name must not be empty

---

## Completion Checklist

- [ ] Completed all "Learn First" topics and wrote notes
- [ ] Finished all task steps
- [ ] Saved deliverable in this folder
- [ ] Wrote 3 things I learned today in `reflection.md`
- [ ] Wrote 1 doubt/blocker (if any) to ask mentor

