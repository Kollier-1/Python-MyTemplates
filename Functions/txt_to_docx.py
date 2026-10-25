"""
Module Name: TXT to DOCX Converter
Description: Reads a plain text file and converts its contents into a Microsoft Word document using the python-docx library.
Author: Kollier
"""

import os
from docx import Document

def convert_txt_to_docx(txt_path: str) -> str:
    if not os.path.isfile(txt_path):
        raise FileNotFoundError(f"File not found: '{txt_path}'")

    base_name, _ = os.path.splitext(txt_path)
    docx_path = f"{base_name}.docx"

    document = Document()

    with open(txt_path, "r", encoding="utf-8") as text_file:
        for line in text_file:
            line_content = line.rstrip("\r\n")
            document.add_paragraph(line_content)

    document.save(docx_path)
    return docx_path

if __name__ == "__main__":
    input_path = input("Enter the path of the TXT file to convert: ").strip()

    try:
        created_file = convert_txt_to_docx(input_path)
        print("\nConversion successful!")
        print(f"Word document created at: {created_file}")

    except FileNotFoundError as error:
        print(f"\nError: {error}")

    except Exception as error:
        print(f"\nAn unexpected error occurred during conversion: {error}")