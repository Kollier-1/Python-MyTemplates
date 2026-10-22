"""
Module Name: Positive Multiple of Five Template
Description: Validates that the user enters a positive integer multiple of five, then calculates and displays its square root.
Author: Kollier
"""

import math

number = int(input("Enter a positive integer that is a multiple of 5: "))

while number <= 0 or number % 5 != 0:
    print("The number is invalid.")
    number = int(input("Please enter the number again: "))

square_root = math.sqrt(number)

print("Entered number:", number)
print("Square root:", square_root)