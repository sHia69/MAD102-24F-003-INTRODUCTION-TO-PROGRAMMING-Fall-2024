# Define a recursive function to calculate the factorial of a number. 
# The factorial of a number is the product of all positive integers less than or equal to the number. 
# For example, the factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120. The factorial of 0 is 1.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
number = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {number} is {factorial(number)}")
