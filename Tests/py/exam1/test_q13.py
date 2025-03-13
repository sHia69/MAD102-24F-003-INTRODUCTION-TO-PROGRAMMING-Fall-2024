# Question 13
# Purpose: B. Write a python number that checks if a given number
# If the number is  dvisible by 2,print  <number> is an even number.
# If the number is not divisible by 2 and leaves reminder 1, print  <number> is a oddnumber
# Non-integer numbers are neither even nor odd, such as 1/2, 0.88, or infinity.  print  <number> is neither even nor odd

num = input('Enter a number: ')

try:
    num = float(num)
    if num.is_integer():
        num = int(num)
        if num % 2 == 0:
            print(f"{num} is an even number")
        else:
            print(f"{num} is an odd number")
    else:
        print(f"{num} is neither even nor odd")
except ValueError:
    print("Error. Please enter a valid number")
