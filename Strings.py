str = "Hello World"

# Print the entire string
print(str)  # Output: Hello World

# Print the first character of the string
print(str[0])  # Output: H

# Print a slice of the string from index 2 to 5
print(str[2:5])  # Output: llo

# Print a slice of the string from index 2 to the end
print(str[2:])  # Output: llo World

# Repeat the string twice
print(str * 2)  # Output: Hello WorldHello World

# Concatenate the string with another string
print(str + " TEST")  # Output: Hello World TEST

# Convert the string to lowercase
print(str.lower())  # Output: hello world  

# Convert the string to uppercase
print(str.upper())  # Output: HELLO WORLD

# Split the string into a list of words
print(str.split())  # Output: ['Hello', 'World']

# Replace a substring with another string
print(str.replace("World", "Python"))  # Output: Hello Python

# Find the index of a substring
print(str.find("World"))  # Output: 6

# Check if the string starts with a substring
print(str.startswith("Hello"))  # Output: True

# Check if the string ends with a substring
print(str.endswith("World"))  # Output: True

# Get the length of the string
print(len(str))  # Output: 11

# Remove leading and trailing whitespace
print(str.strip())  # Output: Hello World

# Count the occurrences of a character
print(str.count("o"))  # Output: 2

# Get the index of a substring
print(str.index("World"))  # Output: 6

# Check if the string is alphanumeric
print(str.isalnum())  # Output: False

# Check if the string is alphabetic
print(str.isalpha())  # Output: False

# Check if the string is a digit
print(str.isdigit())  # Output: False

# Check if the string is lowercase
print(str.islower())  # Output: False

# Check if the string is uppercase
print(str.isupper())  # Output: False

# Check if the string is whitespace
print(str.isspace())  # Output: False

# Check if the string is title case
print(str.istitle())  # Output: True

# Join a list of strings with the string
print(str.join("1234"))  # Output: 1Hello World2Hello World3Hello World4

# Partition the string into three parts
print(str.partition(" "))  # Output: ('Hello', ' ', 'World')

# Find the last index of a substring
print(str.rfind("o"))  # Output: 7

# Get the last index of a substring
print(str.rindex("o"))  # Output: 7

# Right-justify the string
print(str.rjust(20))  # Output: Hello World

# Split the string into a list of words from the right
print(str.rsplit())  # Output: ['Hello', 'World']

# Remove trailing whitespace 
print(str.rstrip())  # Output: Hello World

# Left-justify the string
print(str.ljust(20))  # Output: Hello World        

# Remove leading whitespace
print(str.lstrip())  # Output: Hello World

# Swap the case of the string
print(str.swapcase())  # Output: hELLO wORLD

# Convert the string to title case
print(str.title())  # Output: Hello World

# Pad the string with zeros
print(str.zfill(20))  # Output: 000000000Hello World

# Check if the string is printable
print(str.isprintable())  # Output: True

# Encode the string to bytes
print(str.encode())  # Output: b'Hello World'

# Center the string
print(str.center(20))  # Output:    Hello World     

# Expand tabs in the string
print(str.expandtabs(16))  # Output: Hello World

# Format the string
print(str.format())  # Output: Hello World

# Format the string with a dictionary
print(str.format_map({}))
