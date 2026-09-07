# Day 1 - File Handling
# Reads marks from a text file, handles invalid values, and calculates the average.

def analyze_marks_file(file_path: str) -> tuple[int, float]:
    total = 0
    count = 0

    with open(file_path, "r") as file:
        for line in file:
            value = line.strip()

            if not value:
                continue

            try:
                mark = int(value)
            except ValueError:
                print(f"Skipping invalid mark: {value}")
                continue

            total += mark
            count += 1

    if count == 0:
        raise ValueError("No valid marks found in the file")

    return total, total / count


if __name__ == "__main__":
    total, average = analyze_marks_file("marks.txt")
    print("Total:", total)
    print("Average:", average)
