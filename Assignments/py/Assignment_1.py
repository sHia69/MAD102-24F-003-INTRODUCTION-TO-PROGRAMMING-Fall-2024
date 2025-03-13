# Author: Hia Al Saleh 
# Date: September 12th of the year 2024
# File: Assignment_1
# Purpose: This program sums the test, the quiz and the assignment for the MAD-102 course then calculates for the weighted total.

print("Welcome to the MAD-102 Course Grade Calculator!")
print("Please enter your scores below:")
# In this program I worked with the float for input values because sometimes users may provide non-integers or even decimal numbers.
# For instance, if a user has obtained the score of 32. That is, if a student was to score 5 of 35 on a test, then using a float will let the program manage without posing a problem.


# For test, quiz and assignment scores
test_1 = float(input("Enter Test 1 score (Total of 35): "))
test_2 = float(input("Enter Test 2 score (Total of 35): "))
test_3 = float(input("Enter Test 3 score (Total of 40): "))

quiz_1 = float(input("Enter Quiz 1 score (Total of 10): "))
quiz_2 = float(input("Enter Quiz 2 score (Total of 10): "))
quiz_3 = float(input("Enter Quiz 3 score (Total of 10): "))

assignment_1 = float(input("Enter Assignment 1 score (Total of 20): "))
assignment_2 = float(input("Enter Assignment 2 score (Total of 20): "))
assignment_3 = float(input("Enter Assignment 3 score (Total of 20): "))

# Averages for test, quiz and assignment
test_average = ((test_1 / 35) * 100 + (test_2 / 35) * 100 + (test_3 / 40) * 100) / 3
quiz_average = ((quiz_1 / 10) * 100 + (quiz_2 / 10) * 100 + (quiz_3 / 10) * 100) / 3
assignment_average = ((assignment_1 / 20) * 100 + (assignment_2 / 20) * 100 + (assignment_3 / 20) * 100) / 3

# overall average
overall_avgerage = (test_average * 0.60) + (quiz_average * 0.10) + (assignment_average * 0.30)

print(f"\nTest Average: {int(test_average)}%") # For test average
print(f"Quiz Average: {int(quiz_average)}%") # For quiz average
print(f"Assignment Average: {int(assignment_average)}%") # Assignment average
print(f"Overall Average: {int(overall_avgerage)}%") # Overall Averege 