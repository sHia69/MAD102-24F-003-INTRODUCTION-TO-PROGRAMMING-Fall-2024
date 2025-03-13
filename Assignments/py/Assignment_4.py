# Name: Hia Al Saleh
# Date: October 11th of the year 2024
# File: Assignment_4

# Purpose: Write a Python program that includes two functions: square_properties and rectangle properties.

# Function square_properties
def square_properties(side):
    area = side * side
    perimeter = 4 * side
    return area, perimeter

# Function rectangle_properties
def rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Main function
def main():
    # Variables of the main function
    side = 0
    length = 0
    width = 0

    # Input
    side = float(input("Enter the side of the square: "))
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    # Output
    print("\nSquare Properties")
    area, perimeter = square_properties(side)
    print(f"Area: {area}, Perimeter: {perimeter}")

    print("\nRectangle Properties")
    area, perimeter = rectangle_properties(length, width)
    print(f"Area: {area}, Perimeter: {perimeter}")

main() 