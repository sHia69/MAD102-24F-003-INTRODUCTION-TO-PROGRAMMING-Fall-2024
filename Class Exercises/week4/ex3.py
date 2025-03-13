# Create a countdown program that will count down to 0 from a provided minute value Display the results to the screen

# declare variables
second = 59 
# introduce the program 
print('It\'s a countdown!') 
print('=='*30) 
minute = int(input('Please enter a minute to countdown from:')) 
# display the results 
print(f'Counting down from {minute}:') 

while minute >=0:
  while second >=0:
    print(f'{minute}:{second}')
    second -=1 
  minute -= 1
  second = 59
# end of program 
print('Blast off!')
