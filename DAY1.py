'''CALCULATING THE REMAINDER OF DIVISION'''

dividend = int(input("Enter the number to be divided: "))
divisor = int(input("Enter the number to divide by: "))

remainder = dividend % divisor

print(f"The remainder when {dividend} is divided by {divisor} is {remainder}.")

print("-------------------------------------------------------------")

'''BASIC STRING PRACTICE'''

name = input("What's your name? ")
greeting = "Hello, " + name + "! Welcome to Day 1 of Python."

print(greeting)
print(f"Your name has {len(name)} characters.")
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())

print("-------------------------------------------------------------")

'''BOOLEAN LOGIC AND, OR, NOT'''

likes_python = input("Do you like Python? (yes/no): ").lower() == "yes"
wants_to_code = input("Do you want to become a coder? (yes/no): ").lower() == "yes"

if likes_python and wants_to_code:
    print("You're on the right path! 🚀")
elif likes_python or wants_to_code:
    print("You're halfway there, keep going! 💪")
else:
    print("Give Python a chance 😉")

print("-------------------------------------------------------------")

'''COMPARISON OPERATORS DEMO'''

a = int(input("Enter number A: "))
b = int(input("Enter number B: "))

print(f"Is A equal to B? {a == b}")
print(f"Is A greater than B? {a > b}")
print(f"Is A less than B? {a < b}")
print(f"Is A not equal to B? {a != b}")
