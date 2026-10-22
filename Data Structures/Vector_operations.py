"""
Module Name: Vector Operations Template
Description: Reads two vectors, multiplies their corresponding elements to create a third vector, and calculates its total sum.
Author: Kollier
"""

vector_size = int(input("Enter the size of vectors A and B: "))

vector_a = []
vector_b = []
vector_c = []

print("Enter the elements of vector A:")
for i in range(vector_size):
    number = int(input(f"A[{i}]: "))
    vector_a.append(number)

print("Enter the elements of vector B:")
for i in range(vector_size):
    number = int(input(f"B[{i}]: "))
    vector_b.append(number)

for i in range(vector_size):
    vector_c.append(vector_a[i] * vector_b[i])

print("Vector C:", vector_c)

total_sum = sum(vector_c)

print("Total sum of vector C:", total_sum)