"""
Module Name: Salary Increase Calculator Template
Description: Calculates a 15% salary increase for employees whose salary is $550 or higher.
Author: Kollier
"""

salary = float(input("Enter the employee's salary: $"))

if salary >= 550:
    increase = salary * 0.15
    new_salary = salary + increase

    print(f"Salary increase: ${increase:.2f}")
    print(f"New salary: ${new_salary:.2f}")
else:
    print("The employee does not qualify for a salary increase.")
    print(f"Current salary: ${salary:.2f}")