"""
Module Name: Number Validation Template
Description: Repeatedly requests an integer greater than 12 and less than 20, then determines whether it is even or odd.
Author: Kollier
"""

while True:
    number = int(input("Enter a number greater than 12 and less than 20: "))

    if number > 12 and number < 20:
        break

    print("Invalid number.")

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")