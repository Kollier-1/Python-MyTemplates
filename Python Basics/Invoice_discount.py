"""
Module Name: Invoice Discount Calculator Template
Description: Generates a sales invoice and calculates the applicable discount based on the total sales amount.
Author: Kollier
"""

salesperson = input("Enter the salesperson's name: ")
customer = input("Enter the customer's name: ")
invoice_date = input("Enter the invoice date: ")
invoice_number = input("Enter the invoice number: ")
sales = float(input("Enter the total sales amount: $"))

if sales < 100:
    percentage = 0
elif sales < 500:
    percentage = 0.15
elif sales <= 1000:
    percentage = 0.20
else:
    percentage = 0.30

discount = sales * percentage
total = sales - discount

print("\n========== INVOICE ==========")
print(f"Invoice number: {invoice_number}")
print(f"Date: {invoice_date}")
print(f"Salesperson: {salesperson}")
print(f"Customer: {customer}")
print("-----------------------------")
print(f"Sales: ${sales:.2f}")
print(f"Discount: {percentage * 100:.0f}%")
print(f"Discount amount: ${discount:.2f}")
print(f"Total amount due: ${total:.2f}")
print("=============================")