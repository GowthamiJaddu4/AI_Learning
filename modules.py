# Day 1 - Modules and __name__ == "__main__"

def greet(name: str) -> str:
    return f"Hello, {name}!"


def calculate_cube(number: int) -> int:
    return number ** 3


if __name__ == "__main__":
    # This block runs when this file is executed directly.
    # It does not run when the file is imported as a module.
    print(greet("Gowthami"))
    print("Cube:", calculate_cube(3))
