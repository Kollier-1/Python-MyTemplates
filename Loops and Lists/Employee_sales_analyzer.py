"""
Module Name: Employee Sales Analyzer Template
Description: Collects sales amounts from employees until the user chooses to stop, then calculates the total sales and average sales per employee.
Author: Kollier
"""

total_sales = 0.0
employee_count = 0
continue_entry = "yes"

while continue_entry.lower() == "yes":
    sales = float(input("Enter the employee's sales amount: $"))

    total_sales += sales
    employee_count += 1

    continue_entry = input("Would you like to enter another employee? (yes/no): ")

if employee_count > 0:
    average_sales = total_sales / employee_count
else:
    average_sales = 0

print("\nTotal employees registered:", employee_count)
print(f"Total sales: ${total_sales:.2f}")
print(f"Average sales per employee: ${average_sales:.2f}")