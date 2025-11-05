n = int(input("Enter len of string: "))
s = input("String: ")
l = list(map(int, input("re: ").split(" ")))
for i in range(n):
    j = l[i]
    print(s[j],end="")
