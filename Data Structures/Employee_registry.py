"""
Module Name: Employee Registry Template
Description: Registers five employees and identifies the employee with the highest salary.
Author: Kollier
"""

employee_names = []
employee_ages = []
employee_salaries = []

for i in range(5):
    employee_names.append(input("Enter the employee's name: "))
    employee_ages.append(input("Enter the employee's age: "))
    employee_salaries.append(float(input("Enter the employee's salary: $")))

max_salary_index = 0

for i in range(5):
    if employee_salaries[i] > employee_salaries[max_salary_index]:
        max_salary_index = i

print(
    f"Employee {employee_names[max_salary_index]} "
    f"has the highest salary: ${employee_salaries[max_salary_index]:.2f}"
)