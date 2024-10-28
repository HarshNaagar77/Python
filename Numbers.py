
# Define some numbers
num1 = 10
num2 = 3.5

# Print the numbers
print(num1)  # Output: 10
print(num2)  # Output: 3.5

# Addition
print(num1 + num2)  # Output: 13.5

# Subtraction
print(num1 - num2)  # Output: 6.5

# Multiplication
print(num1 * num2)  # Output: 35.0

# Divisions
print(num1 / num2)  # Output: 2.8571428571428575wz 

# Floor Division
print(num1 // num2)  # Output: 2.0 

# Modulus
print(num1 % num2)  # Output: 0.5

# Exponentiation 
print(num1 ** 2)  # Output: 100

# Absolute value
print(abs(-num1))  # Output: 10

# Round a number
print(round(num2))  # Output: 4

# Convert to integer
print(int(num2))  # Output: 3

# Convert to float
print(float(num1))  # Output: 10.0

# Check if a number is an integer
print(isinstance(num1, int))  # Output: True

# Check if a number is a float
print(isinstance(num2, float))  # Output: True

# Get the maximum of two numbers
print(max(num1, num2))  # Output: 10

# Get the minimum of two numbers
print(min(num1, num2))  # Output: 3.5

# Find the square root
import math
print(math.sqrt(num1))  # Output: 3.1622776601683795
 
# Find the factorial
print(math.factorial(num1))  # Output: 3628800

# Generate a random number
import random
print(random.randint(1, 10))  # Output: Random integer between 1 and 10

# Check if a number is NaN (Not a Number)
print(math.isnan(float('nan')))  # Output: True

# Check if a number is finite
print(math.isfinite(num2))  # Output: True

# Check if a number is infinite
print(math.isinf(float('inf')))  # Output: True

# Get the binary representation of a number
print(bin(num1))  # Output: 0b1010

# Get the octal representation of a number
print(oct(num1))  # Output: 0o12

# Get the hexadecimal representation of a number
print(hex(num1))  # Output: 0xa

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate the sum of a list of numbers
print(sum(numbers))  # Output: 15

# Calculate the average of a list of numbers
print(sum(numbers) / len(numbers))  # Output: 3.0

# Count occurrences of a number in a list
print(numbers.count(3))  # Output: 1

# Find the index of a number in a list
print(numbers.index(4))  # Output: 3

# Sort the list of numbers
print(sorted(numbers, reverse=True))  # Output: [5, 4, 3, 2, 1]

# Reverse the list of numbers
numbers.reverse()
print(numbers)  # Output: [5, 4, 3, 2, 1]