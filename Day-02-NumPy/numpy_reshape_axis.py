# Day 2 - Reshaping and Axis

import numpy as np

numbers = np.arange(1, 13)

# Reshape: number of elements must remain the same
matrix = numbers.reshape(3, 4)

print("Original:", numbers)
print("Reshaped:")
print(matrix)

# Axis 0 -> column-wise operation
print("Column sums:", np.sum(matrix, axis=0))
print("Column means:", np.mean(matrix, axis=0))

# Axis 1 -> row-wise operation
print("Row sums:", np.sum(matrix, axis=1))
print("Row means:", np.mean(matrix, axis=1))
