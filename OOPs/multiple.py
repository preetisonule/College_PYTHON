class Teacher:
    def teach(self):
        return "Teaching..."

class Researcher:
    def research(self):
        return "Researching..."

class Professor(Teacher, Researcher):
    def guide(self):
        return "Guiding students..."

p = Professor()
print(p.teach())
print(p.research())
print(p.guide())
