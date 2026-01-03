"""
05_encapsulation.py

This file demonstrates:
- Public variables
- Protected variables (convention)
- Private variables (name mangling)
- Encapsulation using properties (Pythonic way)
"""


# -------------------------
# PUBLIC VARIABLE
# -------------------------
class PublicStudent:
    def __init__(self, name):
        # Public attribute (accessible everywhere)
        self.name = name


student1 = PublicStudent("Ambady")
print("Public name:", student1.name)

# Anyone can modify it (no protection)
student1.name = "Changed Name"
print("Modified public name:", student1.name)


# -------------------------
# PROTECTED VARIABLE (_)
# -------------------------
class ProtectedStudent:
    def __init__(self, name):
        # Protected attribute (convention-based)
        self._name = name


student2 = ProtectedStudent("Arjun")
print("Protected name (discouraged access):", student2._name)


# -------------------------
# PRIVATE VARIABLE (__)
# -------------------------
class PrivateStudent:
    def __init__(self, name):
        # Private attribute (name mangling)
        self.__name = name

    def get_name(self):
        return self.__name


student3 = PrivateStudent("Rahul")
print("Private name via method:", student3.get_name())

# This will raise an AttributeError if uncommented
# print(student3.__name)

# Name-mangled access (works but BAD practice)
print("Private name via mangling:", student3._PrivateStudent__name)


# -------------------------
# ENCAPSULATION USING PROPERTIES
# -------------------------
class StudentWithProperty:
    def __init__(self, age):
        self._age = age  # internal variable

    @property
    def age(self):
        # Getter
        return self._age

    @age.setter
    def age(self, value):
        # Setter with validation
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value


student4 = StudentWithProperty(19)
print("Initial age:", student4.age)

student4.age = 20
print("Updated age:", student4.age)

# Uncommenting this will raise ValueError
# student4.age = -5


# -------------------------
# KEY TAKEAWAYS
# -------------------------
# - Public: no protection
# - Protected (_): convention-based warning
# - Private (__): name mangling, not true privacy
# - Properties: clean and Pythonic encapsulation
