# set is one of the built in function in python, others are dictionary, list, tuple
# set is unordered no indexing.
# set items are unchangable, but set items can be removed or added.
# no duplicates are allowed in set, True and 1 are same. False and 0 are same.

set1 = {"apple","banana","cat","dude"}
for i in set1:
    print(i, end=" ")       # Random order

print(type(set1))           # <class 'set'>

print("apple" in set1)      # True
print("dog" in set1)        # False

# ADD OR REMOVE ITEMS IN SET

set1.add("orange")
set1.remove("cat")

# Merge sets : .update(), .union()
A = {"Iron man","Spider man","Hulk","Cap"}
B = {"Genius","Broke","pidit","as of USA"}
A.update(B)
for i in A:
    print(i, end=" ")

# Empty the set
A.clear()                   # will show empty set
del A                       # will delete whole set, if tried to print, will raise Error.

# frozenset                 # cant add or remove. it is what it is.
C = frozenset(B)