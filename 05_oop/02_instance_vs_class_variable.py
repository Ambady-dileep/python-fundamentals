class Student: 
    college = "ABC College" # class variable
    
    def __init__(self,name,age):
        self.name = name # instance variable
        self.age = age # instance variable

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old")

s1 = Student("Ambady",19)
s2 = Student("Arjun",16)

s1.introduce()
s2.introduce()
print(s1.college)

# self.variable → belongs to object
# Class.variable → belongs to class