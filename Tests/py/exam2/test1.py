# Question #6 B
# Purpose: Write a Python program that converts a binary number received as user input into its hexadecimal equivalent.

""" - The function should take a binary string as input.
    - It should convert the binary string to a decimal number, then convert the decimal number to a hexadecimal string.
    - The function should display the binary number entered by the user and its hexadecimal equivalent.
    - Ensure hexadecimal output is in uppercase (e.g., "A", "2F")."""

def binary_to_hex(binary):
    decimal = int(binary, 2)
    hexadecimal = hex(decimal)
    return hexadecimal.upper()

def main():
    while True:
        binary = input('Enter a binary number: ')
        try:
            int(binary, 2)
        except ValueError:
            print('Invalid. Please enter a binary number with only 0s and 1s.')
            continue
        hexadecimal = binary_to_hex(binary)
        print(f'Binary: {binary} --->, Hexadecimal: {hexadecimal}')
    
        if input('Would you like to convert another binary number? ') == 'no':
            break
        
if __name__ == '__main__':
    main()