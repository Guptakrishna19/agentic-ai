import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("DB_PATH", "intern.db")

def get_connection():
    db_dir = os.path.dirname(DB_PATH)
    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    
    # Create departments table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS departments (
            department_id INTEGER PRIMARY KEY AUTOINCREMENT,
            department_name TEXT NOT NULL UNIQUE
        )
    """)
    
    # Create employees table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME TEXT NOT NULL,
            SALARY REAL NOT NULL,
            department_id INTEGER,
            FOREIGN KEY (department_id) REFERENCES departments (department_id)
        )
    """)
    
    # Create projects table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            project_id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_name TEXT NOT NULL,
            employee_id INTEGER,
            FOREIGN KEY (employee_id) REFERENCES employees (ID) ON DELETE CASCADE
        )
    """)
    
    # Seed default departments if table is empty
    cursor.execute("SELECT COUNT(*) FROM departments")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("""
            INSERT INTO departments (department_name) VALUES (?)
        """, [("HR",), ("IT",), ("Finance",), ("Marketing",)])
        
    conn.commit()
    conn.close()