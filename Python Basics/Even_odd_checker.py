"""
Module Name: Even and Odd Number Checker Template
Description: Determines whether an integer is even or odd using the modulo operator.
Author: Kollier
"""

number = int(input("Enter an integer: "))

if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")