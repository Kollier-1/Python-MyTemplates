"""
Module Name: Text Lines File Writer Template
Description: Asks the user how many lines of text to enter and saves them to a physical text file.
Author: Kollier
"""

count = int(input("How many lines of text will you enter? "))

with open("FicheroEJ2.txt", "w", encoding="utf-8") as file:
    for number in range(1, count + 1):
        line = input(f"Enter line {number}: ")
        file.write(line + "\n")

print("The content was saved to FicheroEJ2.txt.")