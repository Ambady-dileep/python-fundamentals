# Python OOP – Master Notes

This file is a complete checklist of **Object-Oriented Programming (OOP) concepts in Python**.
Use this as a **revision map** to ensure no core topic is missed.

---

## 1. Basics of OOP
- What is OOP
- Why OOP exists
- Class
- Object
- Attributes
- Methods

---

## 2. Class and Object
- Defining a class
- Creating objects (instances)
- Accessing attributes and methods
- Object lifecycle

---

## 3. The `self` Keyword
- What `self` is
- Why `self` is required
- How Python passes the object automatically
- `Class.method(object)` vs `object.method()`

---

## 4. Variables in OOP
- Local variables
- Instance variables
- Class variables
- Difference between instance vs class variables
- How variables behave across objects

---

## 5. Methods vs Functions
- What is a method
- What is a function
- Key differences
- When to use each
- Why methods receive `self`

---

## 6. Constructor (`__init__`)
- Purpose of `__init__`
- When it runs
- Initializing object state
- Multiple parameters in constructors
- Constructor vs normal method

---

## 7. Encapsulation
- What encapsulation means
- Public variables
- Protected variables (`_variable`)
- Private variables (`__variable`)
- Python’s convention-based encapsulation

---

## 8. Name Mangling
- What name mangling is
- How `__variable` becomes `_ClassName__variable`
- Why name mangling exists
- Name mangling vs true privacy
- Role of name mangling in inheritance

---

## 9. Properties (Pythonic Encapsulation)
- Why properties are needed
- `@property` decorator
- Getter methods
- Setter methods
- Validation using properties
- Why properties are preferred in real-world Python

---

## 10. Inheritance
- What inheritance is
- IS-A relationship
- Code reuse
- Parent class
- Child class
- `super()` keyword
- Method overriding

---

## 11. Protected vs Private in Inheritance
- How protected variables behave
- Why private variables don’t work in child classes
- Role of name mangling in inheritance safety

---

## 12. Method Resolution Order (MRO)
- What MRO is
- Why MRO exists
- `Class.mro()` method
- Order of method lookup
- How Python resolves conflicts

---

## 13. Multiple Inheritance
- What multiple inheritance is
- How Python handles it
- Diamond problem
- Why Python’s MRO prevents ambiguity
- When to avoid multiple inheritance

---

## 14. `super()` in Depth
- `super()` is NOT the parent
- `super()` follows MRO
- How `super()` works in multiple inheritance
- Common beginner mistakes with `super()`

---

## 15. Composition vs Inheritance
- HAS-A vs IS-A relationship
- Why inheritance is often misused
- Why composition is preferred
- Loose coupling
- Dependency injection
- Real-world design decisions

---

## 16. Polymorphism
- What polymorphism means
- Method overriding
- Same method name, different behavior
- Polymorphism via inheritance
- Polymorphism via duck typing
- Eliminating if/else chains

---

## 17. Duck Typing
- “If it walks like a duck…”
- Behavior-based design
- Python’s dynamic typing advantage
- Polymorphism without inheritance

---

## 18. Abstraction
- What abstraction really means
- Interface vs implementation
- Why abstraction exists
- Loose coupling
- Clean APIs

---

## 19. Abstract Base Classes (ABC)
- What an abstract class is
- `abc` module
- `ABC` base class
- `@abstractmethod`
- Enforcing contracts
- Errors when methods are not implemented

---

## 20. OOP Design Principles (Implicitly Covered)
- Encapsulation
- Abstraction
- Inheritance
- Polymorphism
- Open/Closed Principle
- Favor composition over inheritance

---

## Final Note
If you understand **every topic in this file**,  
you understand **Python OOP at an industry level**.

This is not tutorial knowledge.
This is **engineering knowledge**.
