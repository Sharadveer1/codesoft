import random
import string

def get_user_choice(prompt):
    """Helper function to get Yes/No input from the user."""
    while True:
        choice = input(prompt + " (y/n): ").strip().lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        print("Please enter 'y' or 'n'.")

def generate_password(length, use_upper, use_digits, use_symbols):
    characters = list(string.ascii_lowercase)
    
    if use_upper:
        characters += list(string.ascii_uppercase)
    if use_digits:
        characters += list(string.digits)
    if use_symbols:
        characters += list(string.punctuation)

    if not characters:
        print("Error: No character types selected.")
        return None

    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("🛡️ Welcome to the Interactive Password Generator 🛡️")
    print("--------------------------------------------------")

    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Password length must be greater than 0.")
                continue
        except ValueError:
            print("Please enter a valid number for the password length.")
            continue

        print("\nSelect password complexity options:")
        use_upper = get_user_choice("Include uppercase letters?")
        use_digits = get_user_choice("Include digits?")
        use_symbols = get_user_choice("Include special characters (e.g., @, #, $)?")

        password = generate_password(length, use_upper, use_digits, use_symbols)
        if password:
            print("\n🔐 Your Generated Password:")
            print(password)

        again = get_user_choice("\nDo you want to generate another password?")
        if not again:
            print("Thank you for using the Password Generator. Goodbye!")
            break
        print("\n--------------------------------------------\n")

if __name__ == "__main__":
    main()
