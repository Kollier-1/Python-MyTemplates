"""
Module Name: File Vowel Counter Template
Description: Opens a text file, reads its content, and counts the vowels found in it, including accented vowels.
Author: Kollier
"""

try:
    with open("FicheroEJ3.txt", "r", encoding="utf-8") as file:
        content = file.read().lower()

    vowels = 0

    for character in content:
        if character in "aeiouáéíóú":
            vowels += 1

    print("Number of vowels found:", vowels)

except FileNotFoundError:
    print("The file FicheroEJ3.txt was not found.")