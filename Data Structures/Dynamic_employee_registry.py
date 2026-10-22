"""
Module Name: Dynamic Employee Registry Template
Description: Registers a user-defined number of employees and identifies the employee with the highest salary.
Author: Kollier
"""

employee_count = int(input("How many employees would you like to register? "))

employee_names = []
employee_ages = []
employee_salaries = []

for i in range(employee_count):
    print(f"Registering employee {i + 1}")
    employee_names.append(input("Enter the employee's name: "))
    employee_ages.append(input("Enter the employee's age: "))
    employee_salaries.append(float(input("Enter the employee's salary: $")))

if employee_count > 0:
    max_salary_index = 0

    for i in range(employee_count):
        if employee_salaries[i] > employee_salaries[max_salary_index]:
            max_salary_index = i

    print(
        f"Employee {employee_names[max_salary_index]} "
        f"has the highest salary: ${employee_salaries[max_salary_index]:.2f}"
    )
else:
    print("No employees were registered.")