import os
import string
import random

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

def main():
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    everything = lowercase + uppercase + digits + symbols
    
    # Initialize variables first
    user_wants_lowercase = False
    user_wants_uppercase = False
    user_wants_digits = False
    user_wants_symbols = False
    user_wants_everything = False
    
    # Start of main code
    clear_screen()
    print("\n" + "=" * 40)
    print("  PASSWORD GENERATOR")
    print("=" * 40 + "\n")
    
    print("Select character types (e.g., '123' for multiple):\n")
    print("  [1] Lowercase")
    print("  [2] Uppercase")
    print("  [3] Digits")
    print("  [4] Symbols")
    print("  [5] Everything\n")
    
    user_wants = input("Enter your choice(s): ")
    
    # Check each character in their input
    if '1' in user_wants:
        user_wants_lowercase = True
    if '2' in user_wants:
        user_wants_uppercase = True
    if '3' in user_wants:
        user_wants_digits = True
    if '4' in user_wants:
        user_wants_symbols = True
    if '5' in user_wants:
        user_wants_everything = True
    
    # Build char_pool AFTER setting the variables
    char_pool = ''
    if user_wants_lowercase:
        char_pool += lowercase
    if user_wants_uppercase:
        char_pool += uppercase
    if user_wants_digits:
        char_pool += digits
    if user_wants_symbols:
        char_pool += symbols
    if user_wants_everything:
        char_pool += everything
    
    print(f"\nYou selected: {user_wants}")
    print("Awesome choice!\n")
    
    # Ask user for password length
    length = int(input("How long should the password be? "))
    
    # Generate password by picking random characters
    password = ''
    for i in range(length):
        password += random.choice(char_pool)
    
    print("\n" + "-" * 40)
    print(f"Your password: {password}")
    print("-" * 40 + "\n")

if __name__ == "__main__":
    main()