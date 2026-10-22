"""
Module Name: Length Converter Template
Description: A reusable utility for converting meters into multiple units of length.
Author: Kollier
"""

meters = float(input("Enter the length in meters: "))

# Convert to inches

inches = meters * 39.3700787

# Convert to kilometers

kilometers = meters / 1000

# Convert to millimeters

millimeters = meters * 1000

# Convert to centimeters

centimeters = meters * 100

# Convert to miles

miles = meters / 1609.344

print(
f"Conversion completed: Inches = {inches}, "
f"Kilometers = {kilometers}, "
f"Millimeters = {millimeters}, "
f"Centimeters = {centimeters}, "
f"Miles = {miles}"
)