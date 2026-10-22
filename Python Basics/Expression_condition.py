"""
Module Name: Expression Condition Checker Template
Description: Evaluates a mathematical expression and determines whether its result is less than 680.
Author: Kollier
"""

p = int(input("Enter the value of P: "))
q = int(input("Enter the value of Q: "))

result = (p ** 3) + (q ** 4) - (2 * (p ** 2))

if result < 680:
    print("The values satisfy the expression.")
    print(f"P = {p}")
    print(f"Q = {q}")
    print(f"Result = {result}")
else:
    print("The values do not satisfy the expression.")
    print(f"Result = {result}")