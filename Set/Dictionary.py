# it is ordered ds.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# no duplicates are allowed.
# key-value pair

dict = {
    "eren": 9,
    "naruto":10,
    "gojo":9,
    "light":10
}

for i in dict:
    print(i, end=" ")

print(dict["light"])

x = dict.keys() # List of keys
y = dict.values() # List of values