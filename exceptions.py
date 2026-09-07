# Day 1 - Exception Handling

def divide_numbers(a: float, b: float) -> float:
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return 0
    else:
        print("Division successful.")
        return result
    finally:
        print("Division operation completed.")


def convert_to_integer(value: str) -> int:
    try:
        return int(value)
    except ValueError:
        print(f"Invalid integer: {value}")
        return 0


def validate_age(age: int) -> None:
    if age < 0:
        raise ValueError("Age cannot be negative")


if __name__ == "__main__":
    print(divide_numbers(10, 2))
    print(divide_numbers(10, 0))
    print(convert_to_integer("25"))
    print(convert_to_integer("abc"))

    try:
        validate_age(-1)
    except ValueError as error:
        print("Error:", error)
