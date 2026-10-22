"""
Module Name: Purchase Financing Calculator Template
Description: Calculates purchase financing through company funds, a bank loan, and manufacturer credit, including the manufacturer's interest.
Author: Kollier
"""

quantity = int(input("Enter the number of parts: "))
unit_price = float(input("Enter the price per part: $"))

purchase_amount = quantity * unit_price

if purchase_amount > 50000:
    company_funds = purchase_amount * 0.55
    bank_loan = purchase_amount * 0.30
    manufacturer_credit = purchase_amount - company_funds - bank_loan
else:
    company_funds = purchase_amount * 0.70
    bank_loan = 0
    manufacturer_credit = purchase_amount - company_funds

interest = manufacturer_credit * 0.20
manufacturer_payment = manufacturer_credit + interest

print("\n--- FINANCING DETAILS ---")
print(f"Total purchase amount: ${purchase_amount:.2f}")
print(f"Company funds: ${company_funds:.2f}")
print(f"Bank loan: ${bank_loan:.2f}")
print(f"Manufacturer credit: ${manufacturer_credit:.2f}")
print(f"Manufacturer interest: ${interest:.2f}")
print(f"Credit + interest: ${manufacturer_payment:.2f}")