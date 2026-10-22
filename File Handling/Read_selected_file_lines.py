"""
Module Name: Selected File Lines Reader Template
Description: Reads a text file and displays the lines within a range specified by the user.
Author: Kollier
"""

with open('FicheroFísico.txt', 'r') as file:
    lines = file.readlines()

start = int(input("From which line would you like to start reading? "))
end = int(input("Up to which line would you like to read? "))

if 1 <= start <= end <= len(lines):
    for line_number in range(start, end + 1):
        print(f"Line {line_number}: {lines[line_number - 1].rstrip()}")
else:
    print(f"Please enter a range between 1 and {len(lines)}.")