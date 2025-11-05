input = input("enter input: ").split(" ")
a,b, c = input()
# for i in range(len(input)):
#     # if(i == " "):
#     count = count + 1
# print(count)

input = input("enter input: ")
count = 1
i = 0
while(i<len(input)):
    if(input[i]==' '):
        count = count + 1 
    i = i+ 1
print(count)
