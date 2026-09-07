# Day 2 - NumPy Operations, Vectorization and Broadcasting

import numpy as np

numbers = np.array([10, 20, 30, 40])

# Vectorized operations
print("Add 5:", numbers + 5)
print("Subtract 5:", numbers - 5)
print("Multiply by 2:", numbers * 2)
print("Divide by 2:", numbers / 2)

# Broadcasting
marks = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

bonus = np.array([5, 5, 5])
print("Broadcasting result:")
print(marks + bonus)

# Aggregations
print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Minimum:", np.min(numbers))
print("Maximum:", np.max(numbers))
print("Standard deviation:", np.std(numbers))
