# 🔥 DAY8.py – Inheritance, super(), and Polymorphism in Python 🔥

# ✅ 1. Basic Inheritance

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting...")

class Car(Vehicle):
    def honk(self):
        print("Beep beep!")

c = Car("Toyota")
c.start()
c.honk()

print("\n" + "-"*40 + "\n")

# ✅ 2. Constructor Overriding with super()

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def info(self):
        print(f"{self.name} is in grade {self.grade}")

s = Student("Riya", 12)
s.info()

print("\n" + "-"*40 + "\n")

# ✅ 3. Method Overriding and Polymorphism

class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

for animal in [Dog(), Cat(), Animal()]:
    animal.speak()

print("\n" + "-"*40 + "\n")

# ✅ 4. Polymorphism via Functions

class Circle:
    def draw(self):
        print("Drawing a circle")

class Square:
    def draw(self):
        print("Drawing a square")

def render_shape(shape):
    shape.draw()

shapes = [Circle(), Square()]
for shape in shapes:
    render_shape(shape)

print("\n" + "-"*40 + "\n")

# ✅ 5. Duck Typing

class TextEditor:
    def execute(self):
        print("Running text editor...")

class WebBrowser:
    def execute(self):
        print("Launching web browser...")

def run_application(app):
    app.execute()

run_application(TextEditor())
run_application(WebBrowser())

print("\n" + "-"*40 + "\n")

# ✅ 6. isinstance() and issubclass()

class A:
    pass

class B(A):
    pass

a = A()
b = B()

print("isinstance(b, A):", isinstance(b, A))       # True
print("issubclass(B, A):", issubclass(B, A))       # True
print("isinstance(a, B):", isinstance(a, B))       # False

print("\n" + "-"*40 + "\n")

# ✅ 7. Multi-Level Inheritance

class Grandparent:
    def house(self):
        print("House from grandparent")

class Parent(Grandparent):
    def car(self):
        print("Car from parent")

class Child(Parent):
    def bike(self):
        print("Bike from child")

c = Child()
c.house()
c.car()
c.bike()
