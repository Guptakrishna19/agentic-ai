def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

if __name__ == "__main__":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("the sum of", num1, "and", num2, "is", add(num1, num2))
    print("the sub of", num1, "and", num2, "is", subtract(num1, num2))
    print("the mul of", num1, "and", num2, "is", multiply(num1, num2))
    print("the div of", num1, "and", num2, "is", divide(num1, num2))