"""
Module Name: Random Number Analyzer Template
Description: Generates 300 random integers between 1 and 500, calculates the sum of odd numbers, and computes the average of even numbers.
Author: Kollier
"""

import random

odd_sum = 0
even_sum = 0
even_count = 0

for i in range(300):
    number = random.randint(1, 500)

    print(number)

    if number % 2 == 0:
        even_sum += number
        even_count += 1
    else:
        odd_sum += number

if even_count > 0:
    even_average = even_sum / even_count
else:
    even_average = 0

print("\nSum of odd numbers:", odd_sum)
print("Average of even numbers:", even_average)