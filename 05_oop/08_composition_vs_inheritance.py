"""
08_composition_vs_inheritance.py

This file demonstrates:
- Inheritance (IS-A relationship)
- Composition (HAS-A relationship)
- Why composition is usually preferred
"""

# -------------------------
# INHERITANCE (IS-A)
# -------------------------
class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


print("=== Inheritance Example ===")
dog = Dog()
dog.eat()     # inherited behavior
dog.bark()    # own behavior


# -------------------------
# WRONG USE OF INHERITANCE
# -------------------------
class Engine:
    def start(self):
        print("Engine started")


class CarWrong(Engine):   # ❌ WRONG: Car is NOT an Engine
    def drive(self):
        self.start()
        print("Car is driving")


print("\n=== Wrong Inheritance Example ===")
car_wrong = CarWrong()
car_wrong.drive()


# -------------------------
# COMPOSITION (HAS-A)
# -------------------------
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()   # HAS-A relationship

    def drive(self):
        self.engine.start()
        print("Car is driving")


print("\n=== Composition Example ===")
car = Car()
car.drive()


# -------------------------
# FLEXIBILITY OF COMPOSITION
# -------------------------
class ElectricEngine:
    def start(self):
        print("Electric engine started")


class CarFlexible:
    def __init__(self, engine):
        self.engine = engine    # dependency injection

    def drive(self):
        self.engine.start()
        print("Car is driving")


print("\n=== Flexible Composition Example ===")
petrol_car = CarFlexible(Engine())
electric_car = CarFlexible(ElectricEngine())

petrol_car.drive()
electric_car.drive()


# -------------------------
# KEY TAKEAWAYS
# -------------------------
# - Inheritance represents IS-A relationships
# - Composition represents HAS-A relationships
# - Do NOT use inheritance just for code reuse
# - Composition provides flexibility and lower coupling
# - Prefer composition in real-world systems
