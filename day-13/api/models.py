from pydantic import BaseModel


class Employee(BaseModel):
    name: str
    department_id: int
    salary: float