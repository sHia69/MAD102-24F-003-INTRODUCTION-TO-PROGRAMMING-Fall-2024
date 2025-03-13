# Author: Hia Al Saleh
# Date: 29th November of the year 2024
# File: Assignment_10.py

""" 
Purpose: Answer the following questions: 
You must solve the questions using Recursion function. You must answer Question 1 and 2. You
program should handle any exceptions that may arise during runtime.
• Question 1 – 8 Marks
• Question 2 – 12 Marks
-----------------------------------------------------
Question 1B: 
Fibonacci Sequence
In math, this sequence is 0 then 1, then the sum of the previous two numbers 1, then the sum of the
previous two numbers (1, 1) 2, then the sum of the previous two numbers (1,2) 3 etc.
 
Example: 0, 1, 1, 2,3, 5, 8,13, 21, 34,….
Create a python program that uses recursive function to display the Fibonacci sequence until it reaches
n numbers in series. 
Program Implementation :
     1. Get a number as user input 'n' (n>0).
     2. Implement a recursive function to find the print the Fibonacci sequence. You should have n
numbers in your sequence.
Example Input and Output:
(Input) Enter the number (>0): 10
(Output) Fibonacci sequence: 0 1 1 2 3 5 8 13 21 34
"""
# Defining a recursive function to generate the Fibonacci sequence up to n
def fibonacci_sequence(n, a=0, b=1, sequence=[]):
    if a > n:
        return sequence  # Base case: stop when 'a' exceeds 'n'
    sequence.append(a)
    return fibonacci_sequence(n, b, a + b, sequence)  # Recursive call

# Main function
def main():
    num = int(input("Enter a number (>0): "))
    result = fibonacci_sequence(num, 0, 1, [])  # Start with an empty list
    print("Fibonacci sequence up to", num, "is:", result)

# Calling the main function
if __name__ == "__main__":
    main()

"""
Question 2:
Bobble Sort
The bubble sort will sort an array by comparing two elements – and swapping them
▪ The greater value is always placed on the right of the element
▪ The first pass through the array will make sure that the largest value is located on the far right/
end of the array
▪ The largest value bubbles to the top
▪ You will the work your way through the array moving the second highest value to the second last
position, then the third highest value to the third highest position… etc.

Program Implementation:
    1. Get a list with numbers as user input
    2. Implement a recursive function to perform bubble sort
    3. Print the sorted list.
Example Input and Output:
Enter the array elements separated by comma: 1,6,3,6
Sorted array: [1, 3, 6, 6]

"""
# Defining a recursive function to perform bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track if any swaps are made
        swapped = False 
        for j in range(0, n-i-1):
            # Compare the adjacent elements
            if arr[j] > arr[j+1]:
                # Swap if the element found is greater
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no swaps were made, the array is already sorted
        if not swapped:
            break
    return arr

# Main function
def main():
    arr = list(map(int, input("Enter the array elements separated by comma: ").split(',')))
    result = bubble_sort(arr)
    print("Sorted array:", result)
    
# Calling the main function
if __name__ == "__main__":
   main()