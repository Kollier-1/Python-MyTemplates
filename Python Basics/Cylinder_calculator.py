"""
Module Name: Cylinder Calculator Template
Description: Calculates the total surface area and volume of a cylinder using the math module.
Author: Kollier
"""

import math

radius = float(input("Enter the radius: "))
height = float(input("Enter the height: "))

surface_area = 2 * math.pi * radius * (radius + height)
volume = math.pi * radius ** 2 * height

print(f"Surface Area: {surface_area}")
print()
print(f"Volume: {volume}")