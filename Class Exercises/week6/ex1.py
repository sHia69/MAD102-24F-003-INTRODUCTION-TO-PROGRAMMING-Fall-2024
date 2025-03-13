# Function to return the minimum and maximum of two values
def min_max(score1, score2):
    if score1 > score2:
        return score1, score2
    elif score1 < score2:
        return score2, score1
    else:
        return score1, score2  # Both are equal, returning either order doesn't matter

# Function to return the absolute difference between the two scores
def score_difference(score1, score2):
    return abs(score1 - score2)

# Main program for Exercise 1
def main_exercise1():
    # Get the scores from the user
    score1 = int(input("Enter the first player's score: "))
    score2 = int(input("Enter the second player's score: "))

    # Get the highest and lowest scores
    high, low = min_max(score1, score2)

    # Calculate the score difference
    difference = score_difference(high, low)

    # Display the results
    print(f"The highest score is: {high}")
    print(f"The lowest score is: {low}")
    print(f"The difference between the scores is: {difference}")

# Run Exercise 1
main_exercise1()