"""
Module Name: Even Numbers Sum and Product Template
Description: Uses a while loop to calculate the sum and product of even numbers from 10 to 30, inclusive.
Author: Kollier
"""

number = 10
total_sum = 0
total_product = 1

while number <= 30:
    total_sum += number
    total_product *= number

    number += 2

print("Sum of even numbers:", total_sum)
print("Product of even numbers:", total_product)