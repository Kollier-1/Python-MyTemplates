"""
Module Name: Employee Profit-Sharing Calculator Template
Description: Calculates an employee's profit-sharing amount based on their monthly salary and years of service.
Author: Kollier
"""

salary = float(input("Enter the employee's monthly salary: $"))
years_of_service = float(input("Enter the years of service: "))

if years_of_service < 1:
    percentage = 0.05
elif years_of_service < 2:
    percentage = 0.07
elif years_of_service < 5:
    percentage = 0.10
elif years_of_service < 10:
    percentage = 0.15
else:
    percentage = 0.20

profit_sharing = salary * percentage

print(f"\nMonthly salary: ${salary:.2f}")
print(f"Years of service: {years_of_service}")
print(f"Profit-sharing percentage: {percentage * 100:.0f}%")
print(f"Profit-sharing amount: ${profit_sharing:.2f}")