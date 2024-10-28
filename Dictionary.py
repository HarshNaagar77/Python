# Create a dictionary representing a person's profile
person_profile = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York',
    'hobbies': ['reading', 'traveling', 'swimming'],
    'is_student': False
}

# Print the entire dictionary
print(person_profile)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'hobbies': ['reading', 'traveling', 'swimming'], 'is_student': False}

# Access a value by key
print(person_profile['name'])  # Output: Alice

# Add a new key-value pair to the dictionary
person_profile['email'] = 'alice@example.com'
print(person_profile)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'hobbies': ['reading', 'traveling', 'swimming'], 'is_student': False, 'email': 'alice@example.com'}

# Update the value of an existing key
person_profile['age'] = 31
print(person_profile)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'hobbies': ['reading', 'traveling', 'swimming'], 'is_student': False, 'email': 'alice@example.com'}

# Remove a key-value pair by key
del person_profile['is_student']
print(person_profile)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'hobbies': ['reading', 'traveling', 'swimming'], 'email': 'alice@example.com'}

# Get the keys of the dictionary
print(person_profile.keys())  # Output: dict_keys(['name', 'age', 'city', 'hobbies', 'email'])

# Get the values of the dictionary
print(person_profile.values())  # Output: dict_values(['Alice', 31, 'New York', ['reading', 'traveling', 'swimming'], 'alice@example.com'])

# Get the items of the dictionary
print(person_profile.items())  # Output: dict_items([('name', 'Alice'), ('age', 31), ('city', 'New York'), ('hobbies', ['reading', 'traveling', 'swimming']), ('email', 'alice@example.com')])

# Check if a key exists in the dictionary
print('age' in person_profile)  # Output: True
print('gender' in person_profile)  # Output: False

# Get a value with a default if the key does not exist
print(person_profile.get('gender', 'Not Specified'))  # Output: Not Specified

# Clear the dictionary
person_profile.clear()
print(person_profile)  # Output: {}

# Check if the dictionary is empty
print(len(person_profile) == 0)  # Output: True

# Re-create the dictionary for further operations
inventory = {
    'apples': 10,
    'bananas': 5,
    'oranges': 8
}

# Copy the inventory dictionary
copied_inventory = inventory.copy()
print(copied_inventory)  # Output: {'apples': 10, 'bananas': 5, 'oranges': 8}

# Merge two dictionaries
additional_stock = {
    'bananas': 3,
    'grapes': 12
}
inventory.update(additional_stock)
print(inventory)  # Output: {'apples': 10, 'bananas': 8, 'oranges': 8, 'grapes': 12}

# List comprehension to create a new dictionary with items that have more than 6 in stock
high_stock = {k: v for k, v in inventory.items() if v > 6}
print(high_stock)  # Output: {'apples': 10, 'bananas': 8, 'grapes': 12}

# Get the number of key-value pairs in the dictionary
print(len(inventory))  # Output: 4

# Get the maximum and minimum keys in the dictionary (lexicographically)
print(max(inventory))  # Output: 'oranges'
print(min(inventory))  # Output: 'apples'

# Get the total number of fruits in stock
total_stock = sum(inventory.values())
print(total_stock)  # Output: 38