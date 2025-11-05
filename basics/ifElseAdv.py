# programs to find largest and smallest of three nums

a= int(input("Enter a nums: "))
b= int(input("Enter b nums: "))
c= int(input("Enter c nums: "))
if(a>b):
    if(a>c):
        print("a")
    else:
        print("c")
else:
    if(b>c):
        print("b")
    else:
        print("c")

