# GLOBAL VARIABLE
country = "India"


class Student:
    # CLASS VARIABLE (shared by all objects)
    college = "ABC College"

    def __init__(self, name, age):
        # INSTANCE VARIABLES (unique to each object)
        self.name = name
        self.age = age

    def introduce(self):
        # LOCAL VARIABLE (exists only inside this method)
        intro_message = f"My name is {self.name} and I am {self.age} years old"
        print(intro_message)
        print("Country:", country)


# OBJECT CREATION
s1 = Student("Ambady", 19)
s2 = Student("Arjun", 16)

# MODIFY INSTANCE VARIABLE
s1.age = 20

# METHOD CALLS
s1.introduce()
s2.introduce()

# ACCESS CLASS VARIABLE
print("College:", Student.college)
print("College via object:", s1.college)
