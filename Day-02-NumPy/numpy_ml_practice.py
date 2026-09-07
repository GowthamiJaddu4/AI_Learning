# Day 2 - NumPy ML-Style Practice

import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
    [15, 25, 35]
])

# Dataset shape
print("Shape:", data.shape)

# Average for each student
student_averages = np.mean(data, axis=1)
print("Student averages:", student_averages)

# Average for each subject
subject_averages = np.mean(data, axis=0)
print("Subject averages:", subject_averages)

# Students whose average is greater than 50
high_average_students = student_averages[student_averages > 50]
print("Averages greater than 50:", high_average_students)

# Add 5 marks to every value using vectorization
updated_data = data + 5
print("Data after adding 5:")
print(updated_data)

# First two students and last two subjects
selected_data = data[0:2, 1:3]
print("Selected data:")
print(selected_data)
