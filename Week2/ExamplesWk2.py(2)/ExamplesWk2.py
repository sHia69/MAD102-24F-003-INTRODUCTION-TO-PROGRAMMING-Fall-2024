# Program Name: Chocolate Bar Sales Program
# Purpose: Determine what each customer owes
# Author: Bruce Wayne
# Date completed: September 2023

#     Declare variables 
cost_per_bar = 2.45    # cost per chocolate bar
    
#     //Display a welcome message
print('Welcome to my chocolate bar calculation program')

#     Ask for their name
customer = input('Please enter the customer\'s name:')
    
#     Ask for the number of chocolate bars
num_chocolate_bars = input('Please enter the number of chocolate bars to purchase:')
    
#     Calculate the amount owing
total = num_chocolate_bars * cost_per_bar


#     Display our output
print(f'Hello {customer}, you owe ${total} for the purchase of {num_chocolate_bars}.')
    
#     Thank the user
print('Thank you for using the calculator program.')

