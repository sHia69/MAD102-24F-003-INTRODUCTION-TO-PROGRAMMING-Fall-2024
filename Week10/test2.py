# Question #7 B
# Purpose: Write a Python program with the function create_dictionary  that allows the user to input a series of words, organize them by their starting letter, and retrieve words based on a specified letter.

""" - Write a function create_dictionary() that:
    - Prompts the user to enter a string of words separated by commas and spaces (e.g., "Apple, Banana, Avocado, Cherry, apricot, berry").
    - Splits the input string into individual words, removes any leading or trailing whitespace from each word, and converts them to lowercase.
    - Creates a dictionary where:
    - Each key is the lowercase first letter of a word.
    - Each value is a list of all words that start with that letter.
    - Returns the resulting dictionary."""
    
def create_dictionary():
    words = input('Enter a series of words separated by commas and spaces: ')
    words = words.split(', ')
    words = [word.strip().lower() for word in words]
    dictionary = {}
    for word in words:
        first_letter = word[0]
        if first_letter not in dictionary:
            dictionary[first_letter] = []
        dictionary[first_letter].append(word)
    return dictionary

def main():
    while True:
        dictionary = create_dictionary()
        print(dictionary)
        letter = input('Enter the first of words to display: ')
        letter = letter.lower()
        if letter in dictionary:
            print(dictionary[letter])
        else:
            print(f'No words found for letter {letter}')
        if input('Would you like to enter another series of words? ') == 'no':
            break

if __name__ == '__main__':
    main()