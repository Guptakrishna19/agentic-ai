from pydantic import BaseModel
from typing import Optional


class Employee(BaseModel):
    name: str
    department_id: int
    salary: Optional[float] = 0.0