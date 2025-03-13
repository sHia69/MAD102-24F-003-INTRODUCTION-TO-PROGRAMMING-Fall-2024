# We want to keep track of our grocery purchases for a day. We then want to know how much we spent. Some days we may not enter anything – so it should display no amount was spent. The purchases vary from day to day
# Declare variables
purchases = []  # Initialize a list to store purchases
total_amount_spent = 0  # Initialize total amount spent

# Introduce Program
print("Welcome to the Grocery Purchase Tracker!")

# Initial user input
purchased = input("Did you purchase any grocery items today ('yes' or 'no'): ").strip().lower()

# Keep prompting the user for purchases until they choose to stop
while True:
    if purchased != "yes" and purchased != "no":
        purchased = input("Enter valid input ('yes' or 'no'): ").strip().lower()
    
    if purchased == 'no':
        break
    elif purchased == 'yes':
        item = input("Enter item name: ")
        
        while True:
            try:
                price = float(input("Enter the price of the item: $"))
                break  # Exit the loop if the price is valid
            except ValueError:
                print("Invalid price. Please enter a valid number.")
        
        purchases.append((item, price))  # Add the item and price to the list of purchases
        total_amount_spent += price  # Update total amount spent
        # Ask if more purchases are made
        purchased = input("Did you purchase more grocery items today ('yes' or 'no'): ").strip().lower()
# Display the purchases and total amount spent
if purchases:
    print("\nYour purchases for the day:")
    for item, price in purchases:
        print(f"{item}: ${price:.2f}")
    print(f"\nTotal amount spent for the day: ${total_amount_spent:.2f}")
else:
    print("\nNo purchases were made today. No amount was spent.")
# Sample additional loop example (adjusted)
for i, s in enumerate(range(1, 5)):
    print("index", i)
    print(s)
