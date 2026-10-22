"""
Module Name: Weekly Salary Calculator Template
Description: Calculates an employee's weekly salary using regular and overtime hourly rates.
Author: Kollier
"""

hours = float(input("Enter the hours worked during the week: "))

if hours <= 40:
    salary = hours * 4
else:
    overtime_hours = hours - 40
    regular_salary = 40 * 4
    overtime_salary = overtime_hours * 6
    salary = regular_salary + overtime_salary

print(f"Weekly salary: ${salary:.2f}")