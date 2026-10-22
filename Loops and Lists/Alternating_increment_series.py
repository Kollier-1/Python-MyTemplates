"""
Module Name: Alternating Increment Series Template
Description: Generates a numeric series starting at 2, alternates increments of 3 and 2, and calculates the sum of all terms up to 1800.
Author: Kollier
"""

number = 2
total_sum = 0
increment = 3

while number <= 1800:
    print(number, end=" ")

    total_sum += number
    number += increment

    if increment == 3:
        increment = 2
    else:
        increment = 3

print("\n\nTotal sum of the series:", total_sum)