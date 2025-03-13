import random

# Main program for Exercise 2
def main_exercise2():
    # Generate a random number between 1 and 10
    number_to_guess = random.randint(1, 10)

    # Allow the user 3 attempts to guess
    attempts = 3
    for i in range(attempts):
        guess = int(input(f"Attempt {i+1}/{attempts} - Guess the number (1-10): "))

        if guess == number_to_guess:
            print("Congratulations! You've guessed the correct number.")
            break
        elif guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    # If the user does not guess correctly after 3 attempts
    else:
        print(f"Sorry, you've used all attempts. The correct number was {number_to_guess}.")

# Run Exercise 2
main_exercise2()