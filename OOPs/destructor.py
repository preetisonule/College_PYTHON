class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        print(f"Employee {self.name} created.")

    def __del__(self):
        print(f"Destructor called, Employee {self.name} is deleted.")

emp1 = Employee("Preeti", 50000)
emp2 = Employee("Rohan", 60000)

del emp1
del emp2

print("End of program")
