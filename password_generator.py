import random
import string

def generate_password(length, include_symbols=True):
    characters = string.ascii_letters + string.digits  # Letters and digits
    symbols = "!@#$%^&*()-_=+[]{}"  # Symbols to include if requested
    
    if include_symbols:
        characters += symbols
    
    # Generate password by randomly picking from the allowed characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    # Generate and print the password
    password = generate_password(length, include_symbols)
    print("Generated Password:", password)
