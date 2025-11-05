class LivingBeing:
    def breathe(self):
        return "Breathing..."

class Animal(LivingBeing):
    def eat(self):
        return "Eating..."

class Dog(Animal):
    def bark(self):
        return "Woof!"

d = Dog()
print(d.breathe())
print(d.eat())
print(d.bark())
