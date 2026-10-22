"""
Module Name: Element Classification Template
Description: Generates 15 random numbers and classifies them into three groups based on their values.
Author: Kollier
"""

import random

for i in range(15):
    number = random.randint(0, 150)

    if 0 <= number < 50:
        print(f"Numbers in list 1: {number}")
    elif 50 <= number < 100:
        print(f"Numbers in list 2: {number}")
    elif 100 <= number <= 150:
        print(f"Numbers in list 3: {number}")