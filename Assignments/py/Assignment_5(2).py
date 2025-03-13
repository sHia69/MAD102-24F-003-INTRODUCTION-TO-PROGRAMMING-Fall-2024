# Name: Hia Al Saleh
# Date: October 18th of the year 2024
# File: Assignment_5(2)

# Purpose: 2. An anagram is a play on words created by rearranging letters of the original word to make a new word or phrase.
# So, we can say two words are anagrams if they contain all the same letters but in a different order.
# Write a Python porgram that takes two strings from the user and tells if the given strings are anagrams or not.

# Function that checks if two strings are anagrams
def anagram(string1, string2):
    # Convert the strings to uppercase
    string1 = string1.upper()
    string2 = string2.upper()
    
    if sorted(string1) == sorted(string2):
        return True
    else:
        return False

# Function that gets input from user
def word():
    # Get input from user
    print("PLAY ANAGRAM!")
    print("=" * 30)
    word1 = input("Enter Word 1: ")
    word2 = input("Enter word 2: ")

    # Checks if the words are anagram
    if anagram(word1,word2):
        print("=" * 30)
        print("Word 1 & 2 are anagram! ")
        print("=" * 30)
    else:
        print("=" * 30)
        print("Word 1 & 2 are not anagram! ")
        print("=" * 30)
word() # Call the function