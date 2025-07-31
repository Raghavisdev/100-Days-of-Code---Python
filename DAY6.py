# 1. Basic Class with Constructor and Method
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says woof!")

dog1 = Dog("Bruno", "Labrador")
dog1.bark()


# 2. Class vs Instance Variables
class Car:
    wheels = 4  # Class variable

    def __init__(self, brand):
        self.brand = brand  # Instance variable

car1 = Car("Toyota")
car2 = Car("Honda")
print(car1.brand, car1.wheels)
print(car2.brand, car2.wheels)


# 3. Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

c = Cat("Kitty")
c.speak()


# 4. super() to Call Parent Constructor
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Bike(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

b = Bike("Yamaha", "R15")
print(b.brand, b.model)


# 5. Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())
# print(acc.__balance)  # This will give an error: private attribute


# 6. Polymorphism
class Bird:
    def sound(self):
        print("Some generic bird sound")

class Sparrow(Bird):
    def sound(self):
        print("Chirp Chirp")

class Parrot(Bird):
    def sound(self):
        print("Squawk")

birds = [Sparrow(), Parrot()]
for bird in birds:
    bird.sound()


# 7. Magic Methods (dunder methods)
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} - {self.pages} pages"

    def __len__(self):
        return self.pages

b = Book("Python Basics", 300)
print(b)
print(len(b))
