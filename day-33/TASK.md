# Week 7 · Day 3: Docker — Package Your App for Any Machine

**Intern:** Dhruv Lukhi  
**Day:** Day 33  
**Level:** Beginner → Intermediate

---

## Learn First (Complete Before Tasks)

Study these topics **before** you start today's tasks. Take notes in `learn-first-notes.md`.

1. What is Docker? Why "it works on my machine" is a problem
2. Container vs Virtual Machine — simple comparison
3. Dockerfile: recipe to build your app image
4. docker-compose: run multiple services (app + database + redis) together

---

## Today's Tasks

Complete these in order. Do not skip ahead — each step builds on the previous one.

### Step 1
Install Docker Desktop

### Step 2
Write a `Dockerfile` for your FastAPI RAG app

### Step 3
Build and run: `docker build -t rag-app .` then `docker run -p 8000:8000 rag-app`

### Step 4
Write `docker-compose.yml` with your app + Chroma/Redis. Test full stack in containers

---

## Deliverable

Dockerfile + docker-compose.yml + screenshot of app running in Docker

Save all files in this folder (`day-33/`).

---

## Recommended Resources

- Docker for beginners: https://www.youtube.com/watch?v=pg19Z8LL06w
- Dockerfile tutorial: https://docs.docker.com/get-started/docker-concepts/building-images/

---

## Stretch Goal (Optional — if you finish early)

Add a health check endpoint and configure it in Docker

---

## Completion Checklist

- [ ] Completed all "Learn First" topics and wrote notes
- [ ] Finished all task steps
- [ ] Saved deliverable in this folder
- [ ] Wrote 3 things I learned today in `reflection.md`
- [ ] Wrote 1 doubt/blocker (if any) to ask mentor

