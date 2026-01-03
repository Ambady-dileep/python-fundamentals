class Student: 
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old")

s1 = Student("Ambady",19)
s2 = Student("Arjun",16)

s1.introduce()
s2.introduce()