"""
Module Name: Diagonal Matrix Template
Description: Creates and displays a 6x6 matrix with ones on both diagonals and zeros in all other positions.
Author: Kollier
"""

matrix = []

for i in range(6):
    row = []

    for j in range(6):
        if i == j or i + j == 5:
            row.append(1)
        else:
            row.append(0)

    matrix.append(row)

print("6x6 Matrix:")

for row in matrix:
    print(row)