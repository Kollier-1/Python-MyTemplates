"""
Module Name: Investment Interest Calculator Template
Description: Calculates the interest earned on an investment and determines whether the interest will be reinvested based on a threshold of $1,500.
Author: Kollier
"""

investment = float(input("Enter the amount of money invested: $"))
interest_rate = float(input("Enter the interest rate (%): "))

interest = investment * (interest_rate / 100)

print(f"Interest earned: ${interest:.2f}")

if interest > 1500:
    total = investment + interest
    print("The interest will be reinvested.")
    print(f"Final amount in the account: ${total:.2f}")
else:
    print("The interest does not exceed $1,500.")
    print(f"Amount remaining in the account: ${investment:.2f}")