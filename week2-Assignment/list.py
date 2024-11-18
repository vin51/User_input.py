# Create an empty list
my_list = []

# Append elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20) 
my_list.append(30)
my_list.append(40)
print("After appending:", my_list)

# Insert 15 at second position (index 1)
my_list.insert(1, 15)
print("After inserting 15:", my_list)

# Extend list with [50, 60, 70]
my_list.extend([50, 60, 70])
print("After extending:", my_list)

# Remove last element
my_list.pop()
print("After removing last element:", my_list)

# Sort in ascending order
my_list.sort()
print("After sorting:", my_list)

# Find index of 30
index = my_list.index(30)
print("Index of 30:", index)