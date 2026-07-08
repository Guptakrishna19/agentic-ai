# Week 3 Review: Full-Stack APIs & Integrations

During Week 3, I explored building robust HTTP APIs, database connectivity, and full-stack integrations.

## Core Learnings

### 1. RESTful APIs with FastAPI
- Built RESTful resource endpoints mapping HTTP methods to CRUD operations (`GET`, `POST`, `PUT`, `DELETE`).
- Leveraged Pydantic's `BaseModel` for validation of request bodies.
- Handled errors using standard exceptions (`HTTPException` with 404 status codes).

### 2. SQLite Integration
- Connect to lightweight relational databases using Python's built-in `sqlite3` library.
- Managed transactions cleanly (`commit()`) and cursor lifecycle.
- Configured `.row_factory = sqlite3.Row` to easily transform table queries to JSON-serializable Python dict lists.
- Implemented robust schemas utilizing `FOREIGN KEY` constraints.

### 3. Frontend & CORS
- Connected frontends using `fetch()` APIs.
- Handled CORS (Cross-Origin Resource Sharing) middleware configurations to allow clean communication.
- Implemented static file mounting in FastAPI to host static index assets easily.
