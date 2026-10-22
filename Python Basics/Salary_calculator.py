"""
Module Name: Salary Calculator Template
Description: Collects employee information and calculates the final salary after applying deductions.
Author: Kollier
"""

employee_name = input("Enter the employee's name: ")
address = input("Enter the employee's address: ")
phone_number = input("Enter the employee's phone number: ")
net_salary = float(input("Enter the net salary: "))

income_tax = net_salary * 0.10
afp_contribution = net_salary * 0.05
fsv_contribution = net_salary * 0.08

final_salary = net_salary - income_tax - afp_contribution - fsv_contribution
total_deductions = income_tax + afp_contribution + fsv_contribution

print(f"Employee Name: {employee_name}")
print()
print(f"Employee Address: {address}")
print()
print(f"Phone Number: {phone_number}")
print(f"Final Salary: {final_salary}")
print(f"Total Deductions: {total_deductions}")