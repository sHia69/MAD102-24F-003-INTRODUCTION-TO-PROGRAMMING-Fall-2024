class BankAccount:
    def __init__(self, account_number, account_owner, initial_balance=0):
        self.account_number = account_number
        self.account_owner = account_owner
        self.intial_balance = initial_balance
     
    def deposit(self, amount):
        if amount > 0:
            self.intial_balance += amount
            print(f"Hooray! You deposited ${amount}. Your new balance is ${self.intial_balance}.")
        else:
            print(f"Sorry, you can't deposit ${amount}. Please enter a positive amount.")
        return self.intial_balance
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.intial_balance:
                self.intial_balance -= amount
                print(f"Success! You withdrew ${amount}. Your new balance is ${self.intial_balance}.")
            else:
                print(f"Sorry, you can't withdraw ${amount}. Your balance is only ${self.intial_balance}.")
        else:
            print(f"Sorry, you can't withdraw ${amount}. Please enter a positive amount.")
        return 
    
    def display_balance(self):
        print(f"Account Number: {self.account_number}\nAccount Owner: {self.account_owner}\nBalance: ${self.intial_balance}")
        return

def main():
    account_number = input("Enter your account number: ")
    account_owner = input("Enter your name: ")
    initial_balance = float(input("Enter your initial balance: "))
    account = BankAccount(account_number, account_owner, initial_balance)
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            amount = float(input("Enter the amount you want to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter the amount you want to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            account.display_balance()
        elif choice == '4':
            print("Thank you for using the bank app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()            