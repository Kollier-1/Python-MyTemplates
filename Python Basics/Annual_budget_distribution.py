"""
Module Name: Annual Budget Distribution Template
Description: Distributes an annual budget among three hospital departments using predefined percentages.
Author: Kollier
"""

annual_budget = float(input("Enter the annual budget: $"))

pediatrics = annual_budget * 0.30
oncology = annual_budget * 0.40
traumatology = annual_budget * 0.30

print("The annual budget has been distributed as follows:")
print()
print(
    f"Pediatrics: ${pediatrics}, "
    f"Oncology: ${oncology}, "
    f"Traumatology: ${traumatology}"
)