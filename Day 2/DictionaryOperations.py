# Creating a dictionary
student_grades = {"Alice": 90, "Bob": 75, "Charlie": 85}

# Adding a new key-value pair
student_grades["Diana"] = 95

# Removing a key-value pair
del student_grades["Bob"]

# Accessing a value
alice_grade = student_grades["Alice"]

# Iterating over dictionary
for student, grade in student_grades.items():
    print(f"{student}: {grade}")

# Output Alice's grade
print("Alice's Grade:", alice_grade)
