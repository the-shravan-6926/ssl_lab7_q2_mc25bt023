
def validate_numbers(*values):
    for value in values:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("Inputs must be numbers")


def add(a, b):
    validate_numbers(a, b)
    return a + b


def subtract(a, b):
    validate_numbers(a, b)
    return a - b


def multiply(a, b):
    validate_numbers(a, b)
    return a * b


def divide(a, b):
    validate_numbers(a, b)
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def square(a):
    validate_numbers(a)
    return a * a


if __name__ == "__main__":
    print(add(5, 3))
    print(divide(10, 2))
    print(square(4))
