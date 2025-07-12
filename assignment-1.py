# Q.1.

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

# Q.2.

# To save 2D data into a CSV text file as

# A, B, C
# 5, 10, 15
# 6, 11, 16
# 7, 12, 17


data = [['A', 'B', 'C'],
        [5, 10, 15],
        [6, 11, 16],
        [7, 12, 17]]

# Write data to file
with open("matrix.csv", 'w') as f:
    for row in data:
        for val in row:
            if row.index(val) == len(row) - 1:
                f.write(str(val))
            else:
                f.write(str(val) + ', ')
        f.write('\n')

# Read and display file
with open("matrix.csv", 'r') as f:
    for line in f:
        print(line, end='')

# Output:
# A, B, C
# 5, 10, 15
# 6, 11, 16
# 7, 12, 17