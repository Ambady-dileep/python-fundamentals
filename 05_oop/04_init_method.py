"""
This file demonstrates:
- What __init__ is
- When it runs
- Why it is needed
- What happens with and without __init__
"""

# -------------------------
# CLASS WITH __init__
# -------------------------
class StudentWithInit:
    def __init__(self, name, age):
        # __init__ runs automatically after object creation
        # It initializes the object with required data
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old")


# Object creation (calls __init__ automatically)
s1 = StudentWithInit("Ambady", 19)
s1.introduce()


# -------------------------
# CLASS WITHOUT __init__
# -------------------------
class StudentWithoutInit:
    def introduce(self):
        # This will fail if attributes are not set manually
        print(f"My name is {self.name} and I am {self.age} years old")


# Object creation (no initialization happens)
s2 = StudentWithoutInit()

# Uncommenting the next line will raise AttributeError
# s2.introduce()


# Manually adding attributes (bad practice)
s2.name = "Arjun"
s2.age = 16
s2.introduce()


# -------------------------
# KEY TAKEAWAYS
# -------------------------
# - __init__ initializes object data
# - It runs automatically when an object is created
# - Without __init__, objects start empty
# - __init__ ensures objects are in a valid state
