class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self._age = age
        self.__grade = grade

    def display_public(self):
        print(f"Name: {self.name}")

    def _display_protected(self):
        print(f"Age: {self._age}")

    def __display_private(self):
        print(f"Grade: {self.__grade}")
    
    def show_private(self):
        self.__display_private()

s = Student("Preeti", 19, "A")

print(s.name)
s.display_public()

print(s._age)
s._display_protected()

s.show_private();
