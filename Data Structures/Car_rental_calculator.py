"""
Module Name: Car Rental Calculator Template
Description: Calculates car rental charges based on rental duration and optional full insurance coverage.
Author: Kollier
"""

# Fixed rental rates: daily rate and full insurance fee
fixed_rates = (35, 150)

# Collect customer information
customer_name = input("Enter your full name: ")
rental_days = int(input("How many days would you like to rent the vehicle? "))
full_insurance = input("Would you like to purchase full insurance? (YES/NO): ").upper()

# Calculate the base rental cost
base_cost = rental_days * fixed_rates[0]

# Calculate the total amount based on insurance selection
if full_insurance == "YES":
   insurance_cost = fixed_rates[1]
   total = (base_cost + insurance_cost) * 1.10
else:
   insurance_cost = 0
   total = base_cost

# Store customer information in a dictionary
customer = {
    "Name": customer_name,
    "Rental days": rental_days,
    "Full insurance": "Yes" if full_insurance == "YES" else "No"
}

#Add the total amount to the customer dictionary
customer["Total to Pay"] = total

print("--- CUSTOMER INFORMATION ---")
print(customer)