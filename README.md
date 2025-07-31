# 100-Days-of-Code---Python
Beginner to Advanced 🐍
By --> RAGHAV SHARMA

|| This repository is a collection of Python code written over 100 days as I learn and improve my programming skills ||


# Day 1 – Python Basics 🐍

On Day 1, I covered some foundational Python topics through small programs:

### ✅ Scripts I wrote:
- 1st : Find the remainder using `%`
- 2nd : String manipulation and length
- 3rd : Practice with `and`, `or`, `not`
- 4th : Comparison operators like `==`, `<`, `>`

### 👨‍💻 What I Learned:
- Taking user input with `input()`
- Using `int()` to convert strings to numbers
- Boolean expressions and conditional logic
- Basic string methods: `.upper()`, `.lower()`, `len()`


# 📘 Day 2 - Python Basics: Lists, Tuples, Dictionaries & Mutability

This repo covers:

- ✅ Lists (mutable, ordered)
- ✅ Tuples (immutable, ordered)
- ✅ Dictionaries (mutable, key-value pairs)
- ✅ Concept of mutability vs immutability

## 🔸 Lists
- Ordered, mutable collection of elements.
- Supports modification, appending, removing, sorting, etc.

## 🔸 Tuples
- Ordered, immutable sequence.
- Cannot be changed once created.
- Useful for fixed data or unpacking.

## 🔸 Dictionaries
- Key-value pairs.
- Mutable and very fast for lookups.
- Modern Python (3.7+) maintains insertion order.

## 🔸 Mutable vs Immutable
| Type         | Mutable | Examples              |
|--------------|---------|------------------------|
| List         | Yes ✅   | `[1, 2, 3]`            |
| Tuple        | No ❌    | `(1, 2, 3)`            |
| Dictionary   | Yes ✅   | `{"a": 1, "b": 2}`     |
| Integer, Str | No ❌    | `5`, `"hello"`         |

---

# 🧠 Day 3 - Python Basics: Conditionals (`if`, `elif`, `else`), Comparisons & Logic

- ✅ `if`, `else`, and `elif` statements
- ✅ Comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- ✅ Logical operators (`and`, `or`, `not`)
- ✅ Nested conditionals and decision trees

## 🔸 `if`, `elif`, `else`
- Used to make decisions in code.
- Checks whether a condition is **True**, and executes a block accordingly.

Operator	           Meaning Example
==	     Equal to	       a == b
!=	   Not equal to	       a != b
>	   Greater than	       a > b
<	    Less than	       a < b
>=	  Greater or equal	   a >= b
<=	   Less or equal	   a <= b

🔸 Logical Operators Used to combine multiple conditions:

Operator	                             Description Example

and	       True if both are true	     age > 18 and has_ID
or	    True if at least one is true	age > 18 or with_guardian
not	      Inverts the condition	not          is_blocked

## Day 4 - Mastering Python Conditionals: if, elif, else

Control flow is what makes your code intelligent — today we dove deep into conditionals, the very heart of decision-making in Python.

🧠 What Are Conditionals?
Conditionals let your program choose different paths based on data or user input. They answer questions like:

Is this number bigger than that?

Should I allow the user to log in?

What grade should I assign?

🧩 Core Building Blocks
if – Runs a block only if a condition is true.

elif – “Else If” → checks more conditions if the previous ones fail.

else – Runs if nothing above it is true.

Think of it as a decision ladder — your program checks each rung until one fits.

🔐 Logic Behind Decisions
We also explored logical operators like:

and → both conditions must be true

or → at least one condition is true

not → reverses the truth value

These power up your conditionals to handle real-world logic.

🔁 Going Deeper
We looked at:

Nested conditionals – if inside if for deeper decisions

Chained conditions – readable one-liners like if 18 <= age <= 60

Common use cases – grading systems, login verifiers, number checkers

🧠 TL;DR Summary
Concept	Meaning
if	First gate of logic
elif	Additional gates
else	Final fallback
and / or / not	Make conditions smarter & realistic

🎯 Why It Matters
Without conditionals, your program is just a set of static instructions. With them? It becomes adaptive, reactive, intelligent.


📘 Day 5 - Python Functions: From Basics to Advanced 🚀
This repo covers all the important concepts of Python functions through easy-to-understand examples.

🔸 What You Will Learn
How to define and call a function

Difference between print and return

Use of default arguments

Anonymous (lambda) functions

Variable-length arguments: *args, **kwargs

Local vs Global variable scope

🧠 Concepts Covered in Python Functions
🧩 Concept	🧪 Syntax Example	📝 Description
Basic function	def greet():	Defines a simple function with no parameters.
Parameters	def greet(name):	Adds input to make the function dynamic.
Return	return value	Sends data back to the caller from the function.
Default values	def greet(name="User"):	Uses fallback values when arguments aren’t passed.
Lambda function	lambda x: x * 2	Defines a small, anonymous function in one line.
*args	def total(*nums):	Accepts multiple positional arguments as a tuple.
**kwargs	def info(**data):	Accepts multiple keyword arguments as a dictionary.
Scope	global x	Refers to a variable outside the function (global scope).
