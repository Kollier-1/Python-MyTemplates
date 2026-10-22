"""
Module Name: Attendee Age Classifier Template
Description: Classifies event attendees by age, separates admitted and denied attendees into lists, and counts the admitted attendees.
Author: Kollier
"""

admitted = []
denied = []

while True:
    age = int(input("Enter an age (0 or a negative number to stop): "))
    if age <= 0:
        break

    if age >= 18:
        admitted.append(age)
    else:
        denied.append(age)

print("--- ATTENDEE AGE LISTS ---")
print("Admitted:", admitted)
print("Denied:", denied)
print(f"Total admitted attendees: {len(admitted)}")