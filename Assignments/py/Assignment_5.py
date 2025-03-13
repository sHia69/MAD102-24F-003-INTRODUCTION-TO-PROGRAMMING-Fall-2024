# Name: Hia Al Saleh
# Date: October 18th of the year 2024
# File: Assignment_5

# Purpose: 1. Writing a python program that takes two strings as input from the user.
# Then print a new list with the common characters regardless of their case in both strings. 
# All characters in the list must be in uppercase and it should be sorted in ascending order.

# Function that gets the common characters from two strings
def common_characters(string1, string2):
    string1 = string1.upper()
    string2 = string2.upper()
    common_chars = []
    for char in string1:
        if char in string2 and char not in common_chars:
            common_chars.append(char)
    common_chars.sort()
    return common_chars

# Function that gets input from user
def main():
    string1 = input("Enter String 1: ")
    string2 = input("Enter String 2: ")
    common_chars = common_characters(string1, string2)
    print("Common characters: ", common_chars)

main() # Call the function