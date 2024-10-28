# Create a list
my_list = [1, 2, 3, 4, 5]

# Print the entire list
print(my_list)  # Output: [1, 2, 3, 4, 5]

# Print the first element of the list
print(my_list[0])  # Output: 1

# Print a slice of the list from index 1 to 3
print(my_list[1:4])  # Output: [2, 3, 4]

# Print a slice of the list from index 2 to the end
print(my_list[2:])  # Output: [3, 4, 5]

# Repeat the list twice
print(my_list * 2)  # Output: [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# Concatenate the list with another list
print(my_list + [6, 7])  # Output: [1, 2, 3, 4, 5, 6, 7]

# Get the length of the list
print(len(my_list))  # Output: 5

# Append an element to the list
my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Insert an element at a specific index
my_list.insert(0, 0)
print(my_list)  # Output: [0, 1, 2, 3, 4, 5, 6]

# Remove an element by value
my_list.remove(3)
print(my_list)  # Output: [0, 1, 2, 4, 5, 6]

# Pop an element from the list
popped_element = my_list.pop()
print(popped_element)  # Output: 6
print(my_list)  # Output: [0, 1, 2, 4, 5]

# Find the index of an element
print(my_list.index(4))  # Output: 3

# Count the occurrences of an element
print(my_list.count(2))  # Output: 1

# Sort the list
my_list.sort()
print(my_list)  # Output: [0, 1, 2, 4, 5]

# Reverse the list
my_list.reverse()
print(my_list)  # Output: [5, 4, 2, 1, 0]

# Clear the list
my_list.clear()
print(my_list)  # Output: []

# Check if the list is empty
print(len(my_list) == 0)  # Output: True

# Extend the list with another list
my_list.extend([1, 2, 3])
print(my_list)  # Output: [1, 2, 3]

# Copy the list
copied_list = my_list.copy()
print(copied_list)  # Output: [1, 2, 3]

# List comprehension to create a new list
squared_list = [x**2 for x in my_list]
print(squared_list)  # Output: [1, 4, 9]

# Check if an element is in the list
print(2 in my_list)  # Output: True

# Get the maximum and minimum values in the list
print(max(my_list))  # Output: 3
print(min(my_list))  # Output: 1