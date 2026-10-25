"""
Module Name: Text File Writer
Description: Defines a function that receives text as a parameter and saves it to a plain text file.
Author: Kollier
"""

def save_file(text):
    with open("archivo.txt", "w", encoding="utf-8") as file:
        file.write(text)

    print("The file has been saved successfully.")

if __name__ == "__main__":
    text = input("Enter the text you want to save: ")
    save_file(text)