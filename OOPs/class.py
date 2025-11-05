# Basic Class Example
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    
    def display_info(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}")
    
    def update_name(self, new_name):
        self.name = new_name
        print(f"Name updated to {self.name}")

student1 = Student("Preeti", 101)
student2 = Student("Rohan", 102)


student1.display_info()   
student2.display_info()   

student1.update_name("Priya")
student1.display_info()   
