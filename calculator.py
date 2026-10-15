
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def square(a):
    return a * a


if __name__ == "__main__":
    print(add(5, 3))
    print(divide(10, 2))
    print(square(4))
