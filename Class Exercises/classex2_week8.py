# Date: 24/10/2024
# Purpose: This script takes a list of numbers input by the user, calculates the mean, median, and mode of the list, and prints the results.

# Define a function to calculate the mean of a list of numbers
def mean(numbers):
    return sum(numbers) / len(numbers)

# Define a function to calculate the median of a list of numbers
def median(numbers):
    numbers.sort() # Sort the list of numbers
    # If the list has an even number of elements, return the average of the two middle elements
    if len(numbers) % 2 == 0:
        return (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
    else:
        return numbers[len(numbers) // 2]

# Define a function to calculate the mode of a list of numbers
def mode(numbers):
    # Create a dictionary to store the count of each number in the list
    counts = {}
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    # Find the mode(s) by finding the number(s) with the highest count        
    max_count = max(counts.values()) # Find the highest count
    modes = [number for number, count in counts.items() if count == max_count]
    return modes

def main():
    print("Welcome to the mean, median, and mode calculator!")
    numbers = [int(number) for number in input("Enter a list of numbers separated by spaces: ").split()] # Get a list of numbers from the user
    print(f"Mean: {mean(numbers)}") 
    print(f"Median: {median(numbers)}") 
    print(f"Mode: {mode(numbers)}") 

if __name__ == "__main__": # Run the main function if the script is run directly
    main()    