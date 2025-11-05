class LivingBeing:
    def breathe(self):
        return "Breathing..."

class Animal(LivingBeing):
    def eat(self):
        return "Eating..."

class Bird(LivingBeing):
    def fly(self):
        return "Flying..."

class Bat(Animal, Bird):
    def sound(self):
        return "Screech!"

b = Bat()
print(b.breathe())
print(b.eat())
print(b.fly())
print(b.sound())
