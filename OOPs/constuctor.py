class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        print("Constructor is called! Object created.")

    def display(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")

car1 = Car("Tesla", "Model S", 2024)
car2 = Car("BMW", "X5", 2023)

car1.display()   
car2.display()  
