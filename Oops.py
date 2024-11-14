
# 1. Class Definition
class Animal:
    def __init__(self, name, species):
        self.name = name  # Instance variable
        self.species = species  # Instance variable

    def speak(self):
        return f"{self.name} makes a sound."

# 2. Creating Objects
dog = Animal("Buddy", "Dog")
cat = Animal("Whiskers", "Cat")

print(dog.speak())  # Output: Buddy makes a sound.
print(cat.speak())  # Output: Whiskers makes a sound.

# 3. Inheritance
class Dog(Animal):  # Dog class inherits from Animal
    def speak(self):
        return f"{self.name} barks."

class Cat(Animal):  # Cat class inherits from Animal
    def speak(self):
        return f"{self.name} meows."

# 4. Polymorphism
def animal_sound(animal):
    print(animal.speak())

animal_sound(dog)  # Output: Buddy barks.
animal_sound(cat)  # Output: Whiskers meows.

# 5. Encapsulation
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.__balance  # Getter method

# 6. Using Encapsulation
account = BankAccount("Alice", 100)
account.deposit(50)  # Output: Deposited 50. New balance: 150
account.withdraw(30)  # Output: Withdrew 30. New balance: 120
print(account.get_balance())  # Output: 120

# 7. Class Attributes and Methods
class Circle:
    pi = 3.14  # Class attribute

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * (self.radius ** 2)  # Class method using class attribute

# 8. Using Class Attributes
circle = Circle(5)
print(circle.area())  # Output: 78.5

# 9. Static Methods
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

# 10. Using Static Methods
print(MathOperations.add(5, 3))  # Output: 8
print(MathOperations.subtract(5, 3))  # Output: 2

# 11. Class Methods
class Person:
    population = 0  # Class attribute

    def __init__(self, name):
        self.name = name
        Person.population += 1

    @classmethod
    def get_population(cls):
        return cls.population  # Class method to access class attribute

# 12. Using Class Methods
person1 = Person("Alice")
person2 = Person("Bob")
print(Person.get_population())  # Output: 2

# 13. Method Overriding
class Bird(Animal):
    def speak(self):
        return f"{self.name} chirps."

# 14. Using Method Overriding
parrot = Bird("Polly")
print(parrot.speak())  # Output: Polly chirps.

# 15. Abstract Base Classes
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# 16. Using Abstract Base Classes
rectangle = Rectangle(4, 5)
print(rectangle.area())  # Output: 20