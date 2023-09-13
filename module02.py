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