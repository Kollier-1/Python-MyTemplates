"""
Module Name: Hypotenuse Calculator Template
Description: Calculates the hypotenuse of a right triangle using the Pythagorean theorem.
Author: Kollier
"""

side_a = float(input("Enter the length of side A: "))
side_b = float(input("Enter the length of side B: "))

hypotenuse = (side_a + side_b)**0.5

print(f"The length of the hypotenuse is: {hypotenuse}")