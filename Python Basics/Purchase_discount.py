"""
Module Name: Purchase Discount Calculator Template
Description: Calculates a purchase discount based on a number selected by the customer.
Author: Kollier
"""

purchase = float(input("Enter the total purchase amount: $"))
number = int(input("Enter the chosen number: "))

if number < 74:
    percentage = 0.15
else:
    percentage = 0.20

discount = purchase * percentage
final_payment = purchase - discount

print(f"\nPurchase total: ${purchase:.2f}")
print(f"Discount applied: {percentage * 100:.0f}%")
print(f"Discount amount: ${discount:.2f}")
print(f"Final payment: ${final_payment:.2f}")