# Date: 24/10/2024

# This function prompts the user to enter their name and their favorite animal.
# The function continues to prompt the user until they type 'quit'.

# Define a function to prompt the user for their name and favorite animal
def favorite_animals():
    names = []
    animals = []
    while True:
        name = input("Enter your name (or 'quit' to stop): ")
        if name.lower() == 'quit':
            break
        animal = input(f"What's {name}'s favorite animal?: ")
        names.append(name)
        animals.append(animal)
# Printing the lists
    print("\nList of Names:", names)
    print("List of Favorite Animals:", animals)
    print("\nNames and their favorite animals:")
    for i in range(len(names)):
        print(f"{names[i]}'s favorite animal is {animals[i]}")

favorite_animals() # Call the function to start the program