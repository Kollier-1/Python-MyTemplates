"""
Module Name: Invoice Simulator Template
Description: Simulates an invoice by calculating product subtotals, the general subtotal, a 10% income tax withholding or discount, and the final amount due.
Author: Kollier
"""

product_count = int(input("Enter the number of products: "))
general_subtotal = 0.0

print("\n========== INVOICE ==========")

for i in range(product_count):
    print(f"\nProduct {i + 1}")

    product_name = input("Product name: ")
    quantity = int(input("Quantity to purchase: "))
    unit_price = float(input("Unit price: $"))

    subtotal = quantity * unit_price
    general_subtotal += subtotal

    print(f"Subtotal: ${subtotal:.2f}")

print("\n========== SUMMARY ==========")
print(f"General subtotal: ${general_subtotal:.2f}")

income_tax_withholding = general_subtotal * 0.10
print(f"10% income tax withholding/discount: ${income_tax_withholding:.2f}")

final_total = general_subtotal - income_tax_withholding
print(f"Final amount due: ${final_total:.2f}")