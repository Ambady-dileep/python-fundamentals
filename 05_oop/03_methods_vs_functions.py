# -------------------------
# METHOD EXAMPLE
# -------------------------
# A method:
# - Lives inside a class
# - Belongs to an object
# - Automatically receives the object as `self`


class Student:
    def __init__(self, name):
        self.name = name  # instance variable

    def say_name(self):
        print(self.name)


# Object creation
s = Student("Ambady")

# Calling a method
s.say_name()

# Behind the scenes, Python does:
# Student.say_name(s)
# Here, `s` becomes `self`


# -------------------------
# FUNCTION EXAMPLE
# -------------------------
# A function:
# - Lives independently
# - Does NOT belong to any class
# - Works only with the data passed to it


def add(a, b):
    """
    Pure function:
    Same input -> same output
    """
    return a + b


print(add(2, 3))


# -------------------------
# FUNCTION vs METHOD USE CASE
# -------------------------

# Function version ❌
# You must pass all data every time
def introduce_function(name, age):
    print(f"My name is {name} and I am {age} years old")


introduce_function("Ambady", 19)


# Method version ✅
# Data is already stored inside the object
class StudentWithIntroduce:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old")


student = StudentWithIntroduce("Ambady", 19)
student.introduce()


# -------------------------
# INTERVIEW DEFINITIONS
# -------------------------

# Function:
# A function is a block of reusable code that performs a specific task
# and does not belong to any object.

# Method:
# A method is a function defined inside a class that operates on an object
# and receives the object as `self`.
