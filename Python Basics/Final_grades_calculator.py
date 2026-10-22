"""
Module Name: Final Grade Calculator Template
Description: Calculates the final course grade using three assessments with different weight percentages.
Author: Kollier
"""

first_exam_grade = float(input("Enter your first exam grade: "))
second_exam_grade = float(input("Enter your second exam grade: "))
third_exam_grade = float(input("Enter your third exam grade: "))

weighted_grade_1 = first_exam_grade * 0.30
weighted_grade_2 = second_exam_grade * 0.30
weighted_grade_3 = third_exam_grade * 0.40

final_grade = weighted_grade_1 + weighted_grade_2 + weighted_grade_3

print(f"Your final grade for the DLP module is: {final_grade}")