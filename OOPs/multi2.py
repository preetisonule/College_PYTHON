class Grandpa:
    def __init__(self):
        self.gname = "krishna"
    


class Papa(Grandpa):
    def __init__(self):
        super().__init__()
        self.pname = "Nishi"

    
class Son(Papa):

    def __init__(self,myname):
        self.myname = myname
        super().__init__()
        print(f"My grandpa is {self.gname}")
        print(f"My Father is {self.pname}")
        print(f"My name is {self.myname}")

me = Son("viru")


"hyrayfaikh"

arr = [1, 2, 4, 1, 6, 2]
for i in arr:
