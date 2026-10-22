"""
Module Name: Student Grade Calculator Template
Description: Stores student information and grades, then calculates the average grade across three academic periods.
Author: Kollier
"""

# Grades
print("---- STUDENT GRADES ----")
student_id = input("Enter your student ID: ")
degree_code = input("Enter your degree program code: ")

private_identification = (student_id, degree_code)

student_name = input("Enter your full name: ")
degree_program = input("Enter your degree program: ")
course_subject = input("Enter the course subject: ")

print("--- ENTER YOUR GRADES ---")
first_period_grade = float(input("Enter the first-period grade: "))
second_period_grade = float(input("Enter the second-period grade: "))
third_period_grade = float(input("Enter the third-period grade: "))

stored_grades = {
    "first_period_grade": first_period_grade,
    "second_period_grade": second_period_grade,
    "third_period_grade": third_period_grade
}

student = {
    "student_name": student_name,
    "degree_program": degree_program,
    "course_subject": course_subject
}

total = first_period_grade + second_period_grade + third_period_grade
average = total / 3

print("--- STUDENT INFORMATION ---")
print(student)
print(f"Average grade: {average}")