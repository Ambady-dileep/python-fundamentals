class Student:
    """
    This class represents a Student.
    It is a blueprint, not a real student.
    """

    def __init__(self, name, age):
        # Instance variables (data unique to each object)
        self.name = name
        self.age = age

    def introduce(self):
        # Method: behavior of the object
        print(f"My name is {self.name} and I am {self.age} years old")


# Objects (real students created from the class)
s1 = Student("Ambady", 19)
s2 = Student("Arjun", 16)

# Each object calls the same method but uses its own data
s1.introduce()
s2.introduce()
