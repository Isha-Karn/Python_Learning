# Creating an empty set
b= set()
print(type(b))

#Adding the values to the empty set
b.add(4)
b.add(5)
b.add(5) # adding a value repeatedly does not changes a set
# b.add([4,5,6]) # cannot add list inside the set
# b.add({4:5}) # cannot add dictionary inside the set
b.add((4,5,6)) # tuple can be added inside the set.
print(b)

# Length of the set
print(len(b)) #prints the length of the set

# Removal of the item
b.remove(5) # removes 5 from the set b
print(b)

b.pop()
print(b)