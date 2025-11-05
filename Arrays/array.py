import array as arr
arr = arr.array('i',[12,13,14,15,45])  # arr.array(typecode,elements)
s = 5
i = 0
while s > 0:
    print(arr[i],end=" ")
    i = i +1
    s = s-1
