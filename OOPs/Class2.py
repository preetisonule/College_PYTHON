class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def isLong(self, pages):
        if self.pages > 300:
            print("Too Long Book")
        else:
            print("short Book")

class Dog:
    def __init__(self):
        print("Bhau nko khau bhau (Woof!)")


b1 = Book("harry Potter","JK Rowling",400)
print(b1.title)
print(b1.author)
print(b1.pages)
b1.isLong(400)


d1 = Dog()
d2 = Dog()