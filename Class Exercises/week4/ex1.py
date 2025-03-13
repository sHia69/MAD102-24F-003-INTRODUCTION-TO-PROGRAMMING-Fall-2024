# We want to create a program that will add two numbers together and return the result. Unlike previous exercises, we will continue to ask the user for numbers until they no longer want to use our program.
user_choice_to_continue = 'Y'
while user_choice_to_continue == 'Y':
    num1 = int(input('Please enter your first number: '))
    num2 = int(input('Please enter your second number: '))
    sum_result = num1 + num2
    print(f'The sum of {num1} + {num2} = {sum_result}')
    
    user_choice_to_continue = input('Would you like to continue? Y/N: ').upper()
    if user_choice_to_continue not in ['Y', 'N']:
        user_choice_to_continue = input('Invalid input. Please enter Y or N: ')
