"""
Topic:
    File Handling

Concepts:
    Read
    Write
    Append

Approach:
    Use Python's built-in open() function with a context manager
    so that files are automatically closed after use.
"""


# Write initial student names to the file.
with open("students.txt", "w") as file:
    file.write("Rahul\n")
    file.write("Aman\n")
    file.write("Priya\n")


# Read all student names from the file.
with open("students.txt", "r") as file:
    content = file.read()
    print("Current students:")
    print(content)


# Append a new student without overwriting existing data.
with open("students.txt", "a") as file:
    file.write("Neha\n")


# Read the updated file.
with open("students.txt", "r") as file:
    content = file.read()
    print("Updated students:")
    print(content)