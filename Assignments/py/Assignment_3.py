# Author: Hia Al Saleh 
# Date: September 27th of the year 2024
# File: Assignment_3
# Purpose: The purpose of this program is to create an invoices for a company with HST included.

# Welcome message
print("Welcome to the ABC Inc. Invoice! ")

# Variables
hourlyRate = 200 # hourly rate for the consultant
hoursWorked = 0 # number of hours worked
HST = 0.13 # HST rate 13%

# Input
clientName = input("Enter the consultant's name: ")
hoursWorked = float(input("Enter the number of hours worked: "))

# Calculations for the invoice
subtotal = hoursWorked * hourlyRate
hstAmount = subtotal * HST
total = subtotal + hstAmount

# Output using a loop to print the invoice
for i in range(1):
    print("ABC Inc")
    print(f"Consultant: {clientName}")
    print(f"Hours Worked: {hoursWorked}")
    print(f"Subtotal: ${subtotal}")
    print(f"HST: ${hstAmount}")
    print(f"Total: ${total}")
