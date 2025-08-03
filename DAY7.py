# 1. Class with a @classmethod as factory
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data_str):
        name, age = data_str.split('-')
        return cls(name, int(age))

# Using the factory method
student_1 = Student.from_string("Raghav-20")
print(student_1.name, student_1.age)

# 2. Static Method Example
class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

print(Calculator.add(10, 5))

# 3. Decorator: Basic Custom Decorator
def greet_decorator(func):
    def wrapper(name):
        print("Hello,", name)
        func(name)
    return wrapper

@greet_decorator
def say_goodbye(name):
    print("Goodbye,", name)

say_goodbye("Raghav")

# 4. Class Method vs Static Method
class Circle:
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    @staticmethod
    def area(radius):
        return Circle.pi * radius ** 2

c = Circle.from_diameter(10)
print("Radius:", c.radius)
print("Area:", Circle.area(c.radius))

# 5. Chaining decorators
def star_decorator(func):
    def wrapper(*args, **kwargs):
        print("*" * 10)
        func(*args, **kwargs)
        print("*" * 10)
    return wrapper

def hash_decorator(func):
    def wrapper(*args, **kwargs):
        print("#" * 10)
        func(*args, **kwargs)
        print("#" * 10)
    return wrapper

@star_decorator
@hash_decorator
def message():
    print("Welcome to Day 7!")

message()
