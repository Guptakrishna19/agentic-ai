from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import get_connection
from models import Employee

app = FastAPI(
    title="Employee CRUD API",
    description="FastAPI + SQLite CRUD Example",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/employees")
def get_employees():
    conn = get_connection()

    employees = conn.execute(
        "SELECT * FROM employees"
    ).fetchall()

    conn.close()

    return [dict(row) for row in employees]

@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):

    conn = get_connection()

    employee = conn.execute(
        "SELECT * FROM employees WHERE id=?",
        (employee_id,)
    ).fetchone()

    conn.close()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return dict(employee)


@app.post("/employees", status_code=201)
def create_employee(employee: Employee):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO employees (NAME, SALARY, department_id)
        VALUES (?, ?, ?)
        """,
        (
            employee.name,
            employee.salary,
            employee.department_id
        )
    )
    conn.commit()
    employee_id = cursor.lastrowid
    conn.close()
    return {
        "id": employee_id,
        "message": "Employee created"
    }


@app.put("/employees/{employee_id}")
def update_employee(
    employee_id: int,
    employee: Employee
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE employees
        SET name=?,
            department_id=?,
            salary=?
        WHERE id=?
        """,
        (
            employee.name,
            employee.department_id,
            employee.salary,
            employee_id
        )
    )

    conn.commit()

    if cursor.rowcount == 0:
        conn.close()

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    conn.close()

    return {
        "message": "Employee updated"
    }

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM employees
        WHERE id=?
        """,
        (employee_id,)
    )

    conn.commit()

    if cursor.rowcount == 0:
        conn.close()

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    conn.close()

    return {
        "message": "Employee deleted"
    }

