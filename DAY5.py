# 1. Basic Function with No Arguments
def say_hello():
    print("Hello, World!")

say_hello()

# 2. Function with Parameters
def greet(name):
    print(f"Hello, {name}!")

greet("Raghav")

# 3. Function with Return Statement
def add(a, b):
    return a + b

result = add(10, 5)
print("Sum is:", result)

# 4. Function with Default Arguments
def greet(name="User"):
    print(f"Welcome, {name}!")

greet()
greet("Raghav")

# 5. Lambda Function (Anonymous function)
square = lambda x: x ** 2
print("Square of 4:", square(4))

# 6. Function with *args (Variable Positional Arguments)
def total_sum(*numbers):
    return sum(numbers)

print("Total:", total_sum(1, 2, 3, 4, 5))

# 7. Function with **kwargs (Variable Keyword Arguments)
def user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

user_info(name="Raghav", age=20, location="Dehradun")

# 8. Global vs Local Scope
x = 10  # Global variable

def modify():
    global x
    x = 20
    print("Inside function, x =", x)

modify()
print("Outside function, x =", x)
