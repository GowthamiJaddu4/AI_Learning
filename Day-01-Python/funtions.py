# Day 1 - Python Functions

def calculate_square(number: int) -> int:
    return number ** 2


def check_even_odd(number: int) -> str:
    return "Even" if number % 2 == 0 else "Odd"


def calculate_average(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("Cannot calculate average of an empty list")
    return sum(numbers) / len(numbers)


def calculate_total(numbers: list[float]) -> float:
    return sum(numbers)


def calculate_power(base: int, exponent: int) -> int:
    return base ** exponent


def analyze_marks(marks: list[int]) -> tuple[float, int, int]:
    if not marks:
        raise ValueError("Marks list cannot be empty")

    average = calculate_average(marks)
    highest = marks[0]
    lowest = marks[0]

    for mark in marks[1:]:
        if mark > highest:
            highest = mark
        if mark < lowest:
            lowest = mark

    return average, highest, lowest


def demonstrate_args_kwargs(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


if __name__ == "__main__":
    marks = [80, 75, 90, 65, 88]

    print("Square:", calculate_square(5))
    print("Even/Odd:", check_even_odd(7))
    print("Average:", calculate_average(marks))
    print("Total:", calculate_total(marks))
    print("Power:", calculate_power(2, 5))
    print("Marks analysis:", analyze_marks(marks))

    demonstrate_args_kwargs(10, 20, name="Gowthami", subject="Python")
