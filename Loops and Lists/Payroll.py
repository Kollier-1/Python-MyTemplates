"""
Module Name: Payroll Calculator Template
Description: Calculates the final salary of 10 employees, applies a 15% increase to salaries below $800, and computes the total payroll.
Author: Kollier
"""

total_payroll = 0.0

for i in range(1, 11):
    salary = float(input(f"Enter the salary of employee {i}: $"))

    if salary < 800:
        increase = salary * 0.15
        salary = salary + increase

    print(f"Final salary of employee {i}: ${salary:.2f}")

    total_payroll += salary

print(f"\nTotal payroll: ${total_payroll:.2f}")