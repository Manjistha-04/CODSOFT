import random
import string

def generate_password(length, use_upper=True, use_digits=True, use_special=True):
    


    characters = string.ascii_lowercase
    
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    
    if length < 1:
        return "Password length must be at least 1"

    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


try:
    length = int(input("Enter the desired password length: "))
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    
    password = generate_password(length, use_upper, use_digits, use_special)
    print(f"Generated Password: {password}")

except ValueError:
    print("Please enter a valid number for password length.")
