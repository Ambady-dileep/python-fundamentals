"""
This file demonstrates:
- Basic inheritance
- Code reuse
- super()
- Method overriding
- Protected vs Private behavior in inheritance
"""

# -------------------------
# BASE CLASS (PARENT)
# -------------------------
class Person:
    def __init__(self, name):
        self.name = name          # public
        self._role = "Human"      # protected
        self.__secret = "DNA"     # private (name mangling)

    def introduce(self):
        print(f"My name is {self.name}")

    def get_secret(self):
        # Private data accessed via method
        return self.__secret


# -------------------------
# CHILD CLASS
# -------------------------
class Student(Person):
    def __init__(self, name, age):
        super().__init__(name)    # call parent constructor
        self.age = age

    def study(self):
        print("I am studying")

    # Method overriding
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old")


# -------------------------
# OBJECT CREATION
# -------------------------
s = Student("Ambady", 19)

# Inherited method (overridden version is used)
s.introduce()

# Child's own method
s.study()

# Accessing protected variable (works, but discouraged)
print("Role:", s._role)

# Accessing private variable directly ❌ (will fail)
# print(s.__secret)

# Correct way to access private data
print("Secret via method:", s.get_secret())

# Name-mangled access (works but BAD practice)
print("Secret via mangling:", s._Person__secret)


# -------------------------
# KEY TAKEAWAYS
# -------------------------
# - Child class inherits parent attributes and methods
# - super() initializes parent state
# - Method overriding lets child change behavior
# - Protected (_) works in inheritance
# - Private (__) uses name mangling and avoids collisions
