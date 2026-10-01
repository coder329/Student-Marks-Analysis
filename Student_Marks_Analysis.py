# Student Marks Analysis
# Task 1

# Store student marks in a list
marks = [78, 85, 92, 67, 88, 74, 95, 81, 69, 90]

# Calculate total marks
total = sum(marks)

# Calculate average marks
average = total / len(marks)

# Find highest and lowest marks
highest = max(marks)
lowest = min(marks)

# Display results
print("Student Marks Analysis")
print("----------------------")
print("Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", round(average, 2))
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)