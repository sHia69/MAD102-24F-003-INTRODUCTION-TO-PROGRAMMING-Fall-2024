# Resilting Code
student = ["Mal", "Jayne", "Washburn", "Zoe"]
name = input("Please enter a name:")

if name in student:
    print("Welcone - you are registered")
else:
    print("Welcome - you are not on our class list")    

# Membership Operator
firstName = "Edgar"
lastName = "Smith"

anotherName = firstName

if firstName is anotherName:
    print("Same object")
else:
    print("Different object") 

# Ternary Operation
grade = 50
result = "You have passed" if grade >= 50 else "You have failed"
print(result)