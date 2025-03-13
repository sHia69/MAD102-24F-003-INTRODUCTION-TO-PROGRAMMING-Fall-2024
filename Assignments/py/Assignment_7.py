# Author: Hia Al Saleh
# Date: November 5th of the year 2024
# File: Assignment_7.py

# Purpose: Problem Statement:
# Develop a Python program that simulates a bank account system with the following features:
# 1. Account Creation:
# - Allow users to create a bank account by entering their name.
# - Generate a unique 6-digit account number for each new account.
# - Require a minimum deposit of CAD100 to open a new account.
# - Display a success message with the account number upon successful creation.
# 2. Deposit Funds:
# - Enable users to deposit money into their account by providing their account number.
# - Validate the account number and ensure the deposit amount is positive.
# - Display a confirmation message showing the deposited amount and updated balance.
# 3. Withdraw Funds:
# - Allow users to withdraw funds from their account by entering their account number.
# - Check if the withdrawal amount is positive and does not exceed the current balance.
# - Display the new balance or an error message if there are insufficient funds.
# 4. Display Balance:
# - Provide an option for users to view their account balance by entering their account
# number.
# - Display the current balance or an error message if the account number is invalid.
# 5. Exit Program:
# - Allow users to exit the program by choosing the "Exit" option in the menu.
# Requirements:
# - Implement the program using a BankAccount class with attributes and methods to handle account creation, deposits, withdrawals, and balance display.
# - Use a list to store multiple BankAccount objects to manage multiple user accounts.
# - Ensure account numbers are unique and handle invalid inputs gracefully. 
import random

class BankAccount:
    # Method to check if the initial deposit is greater than 100
    def __init__(self, name, initial_deposit):
        self.name = name
        self.account_number = random.randint(100000, 999999)
        self.balance = initial_deposit

    # Defintion of the deposit method
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    # Defintion of the withdraw method
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    # Defintion of the get_balance method
    def get_balance(self):
        return self.balance

# Defining a function to find an account by account number
def find_account(accounts, account_number):
    return next((acc for acc in accounts if acc.account_number == account_number), None)

# Main function to run the program
def main():
    accounts = []

    while True:
        print("\nBank Account Management System")
        print("1. Create Account")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Display Balance")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter your name: ")
            initial_deposit = float(
                input("Enter initial deposit (minimum CAD100): "))
            if initial_deposit >= 100:
                account = BankAccount(name, initial_deposit)
                accounts.append(account)
                print(f"Account created successfully! Your account number is {account.account_number}")
            else:
                print("Initial deposit must be at least CAD100.")

        elif choice in ['2', '3', '4']:
            account_number = int(input("Enter your account number: "))
            account = find_account(accounts, account_number)
            if account:
                if choice == '2':
                    amount = float(input("Enter amount to deposit: "))
                    if account.deposit(amount):
                        print(f"Deposited {amount} successfully. New balance is {account.get_balance()}")
                    else:
                        print("Invalid deposit amount.")
                elif choice == '3':
                    amount = float(input("Enter amount to withdraw: "))
                    if account.withdraw(amount):
                        print(f"Withdrew {amount} successfully. New balance is {account.get_balance()}")
                    else:
                        print("Invalid withdrawal amount or insufficient funds.")
                elif choice == '4':
                    print(f"Your current balance is {account.get_balance()}")
            else:
                print("Account not found.")

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()