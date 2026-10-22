"""
Module Name: Hospitalization Cost Calculator Template
Description: Calculates hospitalization costs, surgery fees, and doctor's fees based on the patient's hospital stay and whether surgery was performed.
Author: Kollier
"""

patient_name = input("Enter the patient's name: ")
days = int(input("Enter the number of days hospitalized: "))
operated = input("Did the patient undergo surgery? (yes/no): ").lower()

hospitalization = days * 25
surgery = 0
doctor_fees = 0

if operated == "yes":
    surgery = 1000
    subtotal = hospitalization + surgery
    doctor_fees = subtotal * 0.20

total = hospitalization + surgery + doctor_fees

print("\n--- PAYMENT DETAILS ---")
print(f"Patient: {patient_name}")
print(f"Days hospitalized: {days}")
print(f"Hospitalization: ${hospitalization:.2f}")
print(f"Surgery: ${surgery:.2f}")
print(f"Doctor's fees: ${doctor_fees:.2f}")
print(f"Total amount due: ${total:.2f}")