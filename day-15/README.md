# Employee Management System

A high-fidelity full-stack Employee Management dashboard built with a **FastAPI** & **SQLite** backend and a modern **Vanilla JavaScript & CSS** frontend.

## Features

- **Full CRUD Operations**: Create new employees, view list, update existing records, and delete employees.
- **Dynamic Search**: Instant client-side search filtering by name, department, or ID.
- **Dynamic Metrics**: Live calculations of total employees and average salary on the dashboard.
- **Interactive Modals**: Seamless editing flow via a slide-in modal.
- **User-Friendly UI/UX**: Custom dropdown menus (fetching departments dynamically), custom input validations, and animated toast notifications.
- **Self-contained static hosting**: Serves static frontend assets directly from port `8000`.

---

## Setup & Running the Application

### 1. Install Dependencies

Make sure your virtual environment is active and install the required dependencies:

```bash
pip install fastapi uvicorn pydantic python-dotenv
```

### 2. Start the Server

Run the backend using the python module command inside the `day-15` directory:

```bash
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### 3. Open the Frontend

Once the server is running, the frontend is served directly. Simply open:

👉 **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

*(Alternatively, you can open `index.html` directly in your browser. The frontend will fallback to `http://127.0.0.1:8000` to call the APIs.)*

---

## Running with Docker & Docker Compose (Stretch Goal)

You can build and deploy the app container using Docker.

### Option A: Using Docker Compose (Recommended)

1. Build and run the container:
   ```bash
   docker-compose up --build -d
   ```
2. Access the portal at: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**.
3. Stop the container:
   ```bash
   docker-compose down
   ```

### Option B: Build and Run Docker Image Manually

1. Build the docker image:
   ```bash
   docker build -t employee-app .
   ```
2. Run the docker container:
   ```bash
   docker run -d -p 8000:8000 --name employee-portal employee-app
   ```
3. Access the portal at: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**.
4. Stop and remove the container:
   ```bash
   docker stop employee-portal && docker rm employee-portal
   ```

