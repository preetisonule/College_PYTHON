class Animal:
    def __init__(self):
        print("this is an animal")

    def speak(self):
        pass

class Dog(Animal):
    def __init__(self):
        print("this is a dog")

    def speak(self):
        print(" Meowww")

class Sparrow:
    def __init__(self):
        print("This is a sparrow")
    def speak(self):
        print("chi chi")

a1 = Dog()
a2 = Sparrow()

