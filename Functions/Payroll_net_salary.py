"""
Module Name: Net Salary Payroll Calculator
Description: Calculates the net salary of multiple employees by applying a 10% income tax withholding, then displays each employee's salary details and the payroll totals.
Author: Kollier
"""

def calculate_income_tax(salary):
    income_tax = salary * 0.10
    return income_tax

def calculate_net_salary(salary, income_tax):
    net_salary = salary - income_tax
    return net_salary

def calculate_payroll():
    employee_count = int(input("Enter the number of employees: "))

    total_net_salary = 0.0
    total_income_tax_withheld = 0.0

    for i in range(employee_count):
        print(f"\nEmployee {i + 1}")

        employee_name = input("Enter the employee's name: ")
        gross_salary = float(input("Enter the gross salary: $"))

        income_tax = calculate_income_tax(gross_salary)
        net_salary = calculate_net_salary(gross_salary, income_tax)

        total_net_salary += net_salary
        total_income_tax_withheld += income_tax

        print(f"\nName: {employee_name}")
        print(f"Gross salary: ${gross_salary:.2f}")
        print(f"Income tax withheld: ${income_tax:.2f}")
        print(f"Net salary: ${net_salary:.2f}")

    print("\n=== EMPLOYEE PAYROLL SUMMARY ===")
    print(f"Total net salaries: ${total_net_salary:.2f}")
    print(f"Total income tax withheld: ${total_income_tax_withheld:.2f}")

if __name__ == "__main__":
    calculate_payroll()