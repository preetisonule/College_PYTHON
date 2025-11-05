class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and my age is {self.age}"
    
class Student(Person):
    def __init__(self, roll_no,name,age):
        super().__init__(name,age)
        self.roll_no = roll_no
    
    def introduce(self):
        print(f"I am a Student also having Roll number : {self.roll_no} and Age : {self.age}")



p2 = Student(27, "Preeti",20)
print(p2.introduce())
