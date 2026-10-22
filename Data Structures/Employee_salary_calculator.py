"""
Module Name: Employee Salary Calculator Template
Description: Calculates an employee's net salary after applying income tax and ISSS deductions, storing the results in a dictionary.
Author: Kollier
"""

# Employees
rates = (0.10, 0.07)

print("--- Employee ---")

employee_name = input("Employee's first name: ")
employee_last_name = input("Employee's last name: ")
base_salary = int(input("Employee's base salary: $"))

income_tax_deduction = base_salary * rates[0]
isss_deduction = base_salary * rates[1]

net_salary = base_salary - income_tax_deduction - isss_deduction

employee = {
    "employee_name": employee_name,
    "employee_last_name": employee_last_name,
    "base_salary": base_salary,
    "income_tax_deduction": income_tax_deduction,
    "isss_deduction": isss_deduction,
    "net_salary": net_salary
}

print("\nEmployee Information:")
print(employee)