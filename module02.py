"""
Description: Module 2 Demonstration.
Author: Karanpreet Singh
Date: September 12, 2023
Usage: Run the application by clicking the run button in the IDE(Integrated Development Environment)
"""

# This is an inline comment.

"""
This is a multiline comment.
It can be span over multiple lines of code.
"""

"""
Constants are defined with uppercase letters.
But there no such thing as 'true' in python. 
"""

PI = 3.1415926
FEDERAL_TAX = 0.05

absolute_value = abs(-12)
print("Absolute value:", absolute_value)
print("Absolute value:"+ str(absolute_value))
print("Absolute value:", abs(-12))

print("I am", "20", "years old")
print("apples", "mangoes", "bananas", sep="**")

# Variables

name = "John"
age = 20
pi = 3.15445
is_a_student = True
salary = 45000
print(type(name))
print(type(age))
print(type(pi))
print(type(is_a_student))

print(f"My name is {name} and I am {age} years old." )
print(f"The value of pi to 2 decimal places is {pi:.2f}")
print(f"Age zero-filled is {age:05}")
print(f"Hello: {name:>10}")
print(f"${salary:,.2f}")

#type conversions
age = 25
salary = 67750.21

age_and_salary = age + salary

months_old = "11"
years_old = 25

age = years_old + (float(months_old) / 12)

print(age)
print(f"Age as a float: {age:.2f}")

age = int(age)
print(age)

# Operators
result = 5 + 5
print(result)

result = 10 - 5
print(result)

result = 5 * 5
print(result)

result = 42 / 4
print(result)

# Integer division

result = 42 // 4
print(result)

# Modulus operator (remainder)

result = 100 % 55
print(result)

# power - raise the first operned to the power of the second
result = 2 ** 4

print(result)

# shortcut operators

age = 25
countdown = 12
factor = 12
half = 11
less_precise_half = 11
remainder = 37
power = 2

# equivalent to age = age + 3
age += 3
countdown -= 1
factor *= 10
half /= 2
less_precise_half //= 2
remainder %= 2
power **= 2