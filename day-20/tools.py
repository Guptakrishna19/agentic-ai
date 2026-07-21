from langchain.tools import tool
from datetime import datetime


@tool
def calculator(expression: str) -> str:
    """Calculate a mathematical expression."""

    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"


@tool
def current_datetime() -> str:
    """Get current date and time."""

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")