import sqlite3
import csv
# Replace this with your actual path
DB_PATH = r"C:\Users\DHRUV\OneDrive\Desktop\intern.db"

# Replace this with your actual path
DB_PATH = r"C:\Users\DHRUV\OneDrive\Desktop\intern.db"


def connect_db():
    try:
        conn = sqlite3.connect(DB_PATH)
        return conn
    except sqlite3.Error as e:
        print("Connection Error:", e)
        return None


def list_employees():
    try:
        conn = connect_db()
        if conn is None:
            return

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()

        if employees:
            print("\n----- Employees -----")
            for emp in employees:
                print(emp)
        else:
            print("No employees found.")

        conn.close()

    except sqlite3.Error as e:
        print("Database Error:", e)


def add_employee():
    try:
        conn = connect_db()
        if conn is None:
            return

        cursor = conn.cursor()

        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        salary = int(input("Enter Salary: "))
        department_id = int(input("Enter Department ID: "))

        cursor.execute(
            """
            INSERT INTO employees (ID, NAME, SALARY, department_id)
            VALUES (?, ?, ?, ?)
            """,
            (emp_id, name, salary, department_id),
        )

        conn.commit()
        conn.close()

        print("Employee added successfully!")

    except sqlite3.IntegrityError:
        print("Employee ID already exists.")

    except sqlite3.Error as e:
        print("Database Error:", e)


def search_employee():
    try:
        conn = connect_db()
        if conn is None:
            return

        cursor = conn.cursor()

        name = input("Enter employee name: ")

        cursor.execute(
            """
            SELECT *
            FROM employees
            WHERE LOWER(NAME) LIKE LOWER(?)
            """,
            ('%' + name + '%',)
        )

        employees = cursor.fetchall()

        if employees:
            print("\nEmployee(s) Found:")
            for emp in employees:
                print(emp)
        else:
            print("No employee found.")

        conn.close()

    except sqlite3.Error as e:
        print("Database Error:", e)


def export_to_csv():
    try:
        conn = connect_db()
        if conn is None:
            return

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()

        with open("employees.csv", "w", newline="") as file:
            writer = csv.writer(file)

            # Column names
            writer.writerow(["ID", "NAME", "SALARY", "department_id"])

            # Employee data
            writer.writerows(employees)

        conn.close()

        print("Employees exported successfully to employees.csv")

    except sqlite3.Error as e:
        print("Database Error:", e)

    except Exception as e:
        print("Error:", e)

def menu():
    while True:
        print("\n===== Employee Management =====")
        print("1. List Employees")
        print("2. Add Employee")
        print("3. Search Employee")
        print("4. Export to CSV")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_employees()

        elif choice == "2":
            add_employee()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            export_to_csv()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()

