"""
Module Name: File Word Counter Template
Description: Opens a text file, reads its content, and counts the words found in it.
Author: Kollier
"""

try:
    with open("FicheroEJ3.txt", "r", encoding="utf-8") as file:
        content = file.read().lower()

    words = content.split()
    print("Number of words found:", len(words))

except FileNotFoundError:
    print("The file FicheroEJ3.txt was not found.")