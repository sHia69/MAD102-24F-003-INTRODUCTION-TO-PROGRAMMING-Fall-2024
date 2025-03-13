# Author: Hia Al Saleh
# Purpose:
# File name: week3.py

income = 56000
creditScore = 800
monthsEmployed = 7

if income >= 4000 and creditScore >= 600:
    print("You have been approved")
elif income >= 40000 and monthsEmployed > 12:
    print("You have been approved") 
elif creditScore >= 600 and monthsEmployed > 12:
    print("You have neen approved")    
else:
    print("You have not been approved")