"""
Module Name: Word Pattern Template
Description: Prints a pattern using a user-provided word with a maximum of four characters.
Author: Kollier
"""

word = input("Enter a word (maximum 4 characters): ")

while len(word) > 4:
      print("The pattern cannot be modified.")
      word = input("Enter a word (maximum 4 characters): ")

print("              *")
print()
print(f"      *      {word}      *")
print()
print(" *     *      *      *     *")