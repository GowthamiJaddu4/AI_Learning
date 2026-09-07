# Day 2 - Boolean Masking

import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
    [15, 25, 35]
])

# Boolean mask
mask = data > 50
print("Boolean mask:")
print(mask)

# Filter values using the mask
filtered_values = data[data > 50]
print("Values greater than 50:")
print(filtered_values)

# Student averages
student_averages = np.mean(data, axis=1)
print("Student averages:", student_averages)

print("Averages greater than 50:")
print(student_averages[student_averages > 50])
