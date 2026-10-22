"""
Module Name: Dynamic Payroll Calculator Template
Description: Repeatedly collects employee base salaries until the user chooses to stop, then calculates the total payroll.
Author: Kollier
"""

total_payroll = 0.0
continue_entry = "yes"

while continue_entry.lower() == "yes":
    salary = float(input("Enter the employee's base salary: $"))

    total_payroll += salary

    continue_entry = input("Would you like to enter another employee? (yes/no): ")

print(f"\nTotal payroll: ${total_payroll:.2f}")