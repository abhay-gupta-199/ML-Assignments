# 1

class DivisionByZeroError(Exception):
    """Exception thrown when attempting to divide by zero."""
    pass

def divide(n1, n2):
    if n2 == 0:
        raise DivisionByZeroError("Division by zero is not allowed.")
    return n1 / n2

# Sample execution 1
try:
    res = divide(23, 5)
    print(res)
except DivisionByZeroError as err:
    print(f"Error: {err}")

    # Output => 4.6

# Sample execution 2
try:
    res = divide(25, 0)
    print(res)
except DivisionByZeroError as err:
    print(f"Error: {err}")

    # Output => Error: Division by zero is not allowed.