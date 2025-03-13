def longest_word():
    longest = ""
    while True:
        word = input("Enter a word (or type 'done' to finish): ").strip()
        if word.lower() == "done":
            break
        
        if len(word) > len(longest):
            longest = word
        elif len(word) == len(longest):
            print(f"'{word}' and '{longest}' have the same length.")

    print(f"The longest word entered is: '{longest}'")
longest_word()