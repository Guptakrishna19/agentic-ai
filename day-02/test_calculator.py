from calculator import add, subtract, multiply, divide

# Test add
assert add(2, 3) == 5
assert add(-1, 1) == 0

# Test subtract
assert subtract(10, 4) == 6
assert subtract(5, 10) == -5

# Test multiply
assert multiply(3, 4) == 12
assert multiply(-2, 5) == -10

# Test divide
assert divide(10, 2) == 5
assert divide(9, 3) == 3

# Test division by zero
assert divide(5, 0) == "Error: Cannot divide by zero."

print("All tests passed!")