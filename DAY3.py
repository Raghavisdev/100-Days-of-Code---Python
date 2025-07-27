#DAY 3: f-else, Elif, Comparison & Logical Operators

# Check if number is even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

print('-------------------------------------------')

# Grade calculator
marks = int(input("Enter your score: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Fail")

print('-------------------------------------------')

# Login system
username = input("Enter your username: ")

if username == "admin":
    print("Welcome, admin!")
elif username == "guest":
    print("Hello, guest user!")
else:
    print("Access Denied")

print('-------------------------------------------')

# Age and license check
age = int(input("Enter your age: "))
has_license = input("Do you have a license? (yes/no): ")

if age >= 18 and has_license.lower() == "yes":
    print("You're allowed to drive.")
elif age >= 18 and has_license.lower() == "no":
    print("You need a license to drive.")
else:
    print("You're too young to drive.")

print("--------------------------------------------")

# ATM access example
card_inserted = input("Is your card inserted? (yes/no): ")
pin = input("Enter your 4-digit PIN: ") if card_inserted.lower() == "yes" else None

if card_inserted.lower() == "yes":
    if pin == "1234":
        print("Access granted.")
    else:
        print("Incorrect PIN.")
else:
    print("Please insert your card.")


