"""
09_polymorphism.py

This file demonstrates:
- Polymorphism via inheritance (method overriding)
- Polymorphism via duck typing
- Why polymorphism removes if/else chains
"""

# -------------------------
# POLYMORPHISM USING INHERITANCE
# -------------------------
class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def speak(self):
        print("Dog barks")


class Cat(Animal):
    def speak(self):
        print("Cat meows")


print("=== Polymorphism with Inheritance ===")
animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()   # Same method, different behavior


# -------------------------
# WHY POLYMORPHISM IS POWERFUL
# -------------------------
"""
Without polymorphism, we would write ugly if/else code.
With polymorphism, behavior is decided by the object itself.
"""


# -------------------------
# POLYMORPHISM WITHOUT INHERITANCE (DUCK TYPING)
# -------------------------
class Car:
    def move(self):
        print("Car is moving")


class Person:
    def move(self):
        print("Person is walking")


class Robot:
    def move(self):
        print("Robot is rolling")


print("\n=== Duck Typing Polymorphism ===")
objects = [Car(), Person(), Robot()]

for obj in objects:
    obj.move()   # Python only cares about method existence


# -------------------------
# REAL-WORLD EXAMPLE
# -------------------------
class FileLogger:
    def log(self, message):
        print(f"File log: {message}")


class DatabaseLogger:
    def log(self, message):
        print(f"Database log: {message}")


def log_message(logger):
    logger.log("System started")


print("\n=== Real-world Polymorphism ===")
log_message(FileLogger())
log_message(DatabaseLogger())


# -------------------------
# KEY TAKEAWAYS
# -------------------------
# - Same method name, different behavior
# - Achieved via inheritance or duck typing
# - Eliminates if/else conditions
# - Makes code extensible and clean
