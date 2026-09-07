# Day 2 - NumPy Basics

import numpy as np

# Creating arrays
numbers = np.array([10, 20, 30, 40, 50])
zeros = np.zeros(5)
ones = np.ones(5)
range_array = np.arange(1, 6)
even_numbers = np.arange(0, 10, 2)
linearly_spaced = np.linspace(0, 1, 5)

print("Array:", numbers)
print("Zeros:", zeros)
print("Ones:", ones)
print("Arange:", range_array)
print("Even numbers:", even_numbers)
print("Linspace:", linearly_spaced)

# Dimensions and shape
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Dimensions:", matrix.ndim)
print("Shape:", matrix.shape)
print("Number of elements:", matrix.size)

# Indexing
print("First element:", numbers[0])
print("Matrix element:", matrix[0, 1])
