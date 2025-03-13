def is_valid_password(password):
    if len(password) < 10:
        return False

    if not password.isalnum():
        return False

    return True

def password_check():
    password = input("Enter your password: ").strip()
    if is_valid_password(password):
        print("Password is valid.")
    else:
        print("Invalid password. Ensure it is at least 10 characters and contains only letters and numbers.")

password_check()