# Create a program that will count down from a specific number to 0.

# introduce the program
print('It\'s a countdown!')
print('==' * 30)
number = int(input('Please enter a number to countdown from:'))
# display the results
print(f'Counting down from {number}:')
while number > -1:
  print(number)
  number -= 1
# end of program
print('Your Program Ends here!')
