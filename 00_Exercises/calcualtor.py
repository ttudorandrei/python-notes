def add(a: int, b: int):
    if a.isnumeric() and b.isnumeric():
        return a + b
    else:
        return "Please enter a number"


def subtract(a: int, b: int):
    if a.isnumeric() and b.isnumeric():
        return a - b
    else:
        return "Please enter a number"


def multiply(a: int, b: int):
    if a.isnumeric() and b.isnumeric():
        return a * b
    else:
        return "Please enter a number"


def divide(a: int, b: int):
    if a.isnumeric() and b.isnumeric():
        return a / b
    else:
        return "Please enter a number"

