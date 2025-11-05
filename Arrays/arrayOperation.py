import array as arr
arr = arr.array('i',[12,13,14,15,45])  # arr.array(typecode,elements)
s = len(arr)
i = 0
print("Original array")
while s > 0:
    print(arr[i],end=" ")
    i = i +1
    s = s-1

s = len(arr)
# Append()
arr.append(3)
arr.append(7)
arr.append(7)

print("")
print("Append array")
for i in range (len(arr)):
    print (arr[i], end=" ")

# insert()
arr.insert(1,6)
s = len(arr)
print("")
print("insert array")
for i in range (len(arr)):
    print (arr[i], end=" ")

# pop
arr.pop()
arr.pop()
s = len(arr)
print("")
print("pop array")
for i in range (len(arr)):
    print (arr[i], end=" ")

# remove
arr.remove(12)
s = len(arr)
print("")
print("remove array")
for i in range (len(arr)):
    print (arr[i], end=" ")

# index()
print("")
i = arr.index(13)
s = len(arr)
print(i)

# reverse()
arr.reverse()
s = len(arr)
print("reverse array")
for i in range (len(arr)):
    print (arr[i], end=" ")

