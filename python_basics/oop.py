"""
Topic:
    Object-Oriented Programming

Concepts:
    Class
    Object
    Constructor
    Instance Variables
    Methods
"""


class Student:
    def __init__(self, name, age, course):
        # Store student-specific information inside the object.
        self.name = name
        self.age = age
        self.course = course

    def display_details(self):
        # Display the information stored in the object.
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")


# Create an object from the Student class.
student = Student("Krishna", 23, "Biotechnology")

student.display_details()