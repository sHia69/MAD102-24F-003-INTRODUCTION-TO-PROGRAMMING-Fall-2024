def decimal_to_binary(decimal_number):
    return bin(decimal_number)[2:]

def binary_to_decimal(binary_number):
    return int(binary_number, 2)

def decimal_to_hexadecimal(decimal_number):
    return hex(decimal_number)[2:]

def hexadecimal_to_decimal(hexadecimal_number):
    return int(hexadecimal_number, 16)

def main():
    while True:
        print("Select an option:")
        print("1. Convert a decimal number to binary")
        print("2. Convert a binary number to decimal")
        print("3. Convert a decimal number to hexadecimal")
        print("4. Convert a hexadecimal number to decimal")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            decimal_number = int(input("Enter a decimal number: "))
            print(f"Binary: {decimal_to_binary(decimal_number)}")
        elif choice == '2':
            binary_number = input("Enter a binary number: ")
            print(f"Decimal: {binary_to_decimal(binary_number)}")
        elif choice == '3':
            decimal_number = int(input("Enter a decimal number: "))
            print(f"Hexadecimal: {decimal_to_hexadecimal(decimal_number)}")
        elif choice == '4':
            hexadecimal_number = input("Enter a hexadecimal number: ")
            print(f"Decimal: {hexadecimal_to_decimal(hexadecimal_number)}")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()