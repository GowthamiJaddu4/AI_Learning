# Day 2 - NumPy Indexing and Slicing

import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
    [15, 25, 35]
])

# 1D-style row/column selection
print("First row:", data[0])
print("Second column:", data[:, 1])

# 2D indexing
print("Row 1, Column 2:", data[0, 1])

# Slicing: start included, stop excluded
print("First two rows:")
print(data[0:2])

print("Last two columns:")
print(data[:, 1:3])

print("First two rows and last two columns:")
print(data[0:2, 1:3])
