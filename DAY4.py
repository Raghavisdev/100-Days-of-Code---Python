# Day 4 - Loops in Python: for, while, range, break, continue, pass

# ----------------------------------------------------------
# FOR LOOPS
# ----------------------------------------------------------

# Basic iteration using a for loop
print("\n👉 Basic for loop:")
for i in range(5):
    print(f"Number: {i}")

# Iterating over a list
print("\n👉 Loop over a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# Loop with index using enumerate
print("\n👉 Using enumerate():")
for index, fruit in enumerate(fruits):
    print(f"Index {index} has fruit: {fruit}")

# Nested loop
print("\n👉 Nested loop:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i},{j})", end='  ')
    print()

# ----------------------------------------------------------
# WHILE LOOPS
# ----------------------------------------------------------

print("\n👉 Basic while loop:")
count = 0
while count < 3:
    print(f"Count is: {count}")
    count += 1

# Example with user input (commented out for safety)
# while True:
#     user_input = input("Type 'exit' to quit: ")
#     if user_input.lower() == 'exit':
#         break

# ----------------------------------------------------------
# RANGE FUNCTION
# ----------------------------------------------------------

print("\n👉 Using range():")
for i in range(2, 11, 2):  # start=2, stop=11, step=2
    print(i)

# Reversing a range
print("\n👉 Reverse range:")
for i in range(10, 0, -1):
    print(i)

# ----------------------------------------------------------
# LOOP CONTROL STATEMENTS
# ----------------------------------------------------------

# break: exits the loop
print("\n👉 break example:")
for i in range(10):
    if i == 5:
        print("Breaking at 5")
        break
    print(i)

# continue: skips current iteration
print("\n👉 continue example:")
for i in range(5):
    if i == 2:
        print("Skipping 2")
        continue
    print(i)

# pass: does nothing (useful as a placeholder)
print("\n👉 pass example:")
for i in range(3):
    if i == 1:
        pass  # Placeholder
    print(f"Number: {i}")

# ----------------------------------------------------------
# BONUS: Loop with else
# ----------------------------------------------------------

print("\n👉 for loop with else:")
for i in range(3):
    print(i)
else:
    print("Loop completed successfully.")

print("\n👉 while loop with else:")
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("While loop completed successfully.")

# ----------------------------------------------------------
# EXTRA: Looping through dictionary
# ----------------------------------------------------------

print("\n👉 Looping through dictionary:")
students = {"Alice": 85, "Bob": 90, "Charlie": 78}
for name, score in students.items():
    print(f"{name} scored {score}")

# End of Day 4 exampleS