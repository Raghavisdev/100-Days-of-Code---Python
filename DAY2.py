# Day 2: Python Data Structures - Lists, Tuples, Dictionaries

print("🔸 LISTS (Mutable, Ordered)")

# Creating a list
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

# Modifying elements
fruits[1] = "mango"
print("After modifying index 1:", fruits)

# Adding elements
fruits.append("orange")
print("After appending:", fruits)

# Removing an element
fruits.remove("apple")
print("After removing 'apple':", fruits)

# Length of list
print("Length of list:", len(fruits))

print('----------------------------------------------')


print("\n🔸 TUPLES (Immutable, Ordered)")

# Creating a tuple
coordinates = (10.5, 20.3)
print("Tuple:", coordinates)

# Trying to modify (uncomment below to see error)
# coordinates[0] = 15.0  # TypeError

# Tuple unpacking
x, y = coordinates
print("Unpacked values -> x:", x, ", y:", y)

print('-----------------------------------------------------')

print("\n🔸 DICTIONARIES (Mutable, Key-Value, Ordered)")

# Creating a dictionary
student = {
    "name": "Raghav",
    "age": 20,
    "courses": ["Python", "AI"]
}
print("Original dictionary:", student)

# Accessing values
print("Name:", student["name"])

# Modifying values
student["age"] = 21
print("Updated age:", student["age"])

# Adding a new key-value pair
student["college"] = "XYZ University"
print("Added college:", student)

# Getting keys and values
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))

print('----------------------------------------------------')

print("\n🔸 MUTABLE vs IMMUTABLE")

# Mutable example
a = [1, 2, 3]
b = a
b.append(4)
print("Mutable - Original list after modifying b:", a)  # a also changes

# Immutable example
x = 5
y = x
y += 1
print("Immutable - Original int x after y += 1:", x)  # x remains the same
