import random
import string
#import pyperclip

def generate_weak_password():
    # Common passwords for weak passwords
    common_passwords = ["password", "123456", "qwerty", "abc123", "letmein", "welcome", "admin"]
    return random.choice(common_passwords)

def generate_strong_password(length):
    # Generate a strong password with letters and digits
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_hard_password(length):
    # Generate a hard password with letters, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    try:
        # Ask user to choose password strength
        password_strength = input("Choose password strength (weak/strong/hard): ").lower()

        if password_strength == "weak":
            generated_password = generate_weak_password()
        else:
            # For strong and hard passwords, ask for desired length
            password_length = int(input("Enter the desired length for the password: "))
            if password_length <= 0:
                print("Please enter a valid positive length.")
                return

            if password_strength == "strong":
                generated_password = generate_strong_password(password_length)
            elif password_strength == "hard":
                generated_password = generate_hard_password(password_length)
            else:
                print("Invalid password strength. Please choose weak, strong, or hard.")
                return

        # Display the generated password
        print("\nGenerated Password:")
        print(generated_password)

        # Copy to clipboard
       # pyperclip.copy(generated_password)
       # print("Password copied to clipboard.")

    except ValueError:
        print("Please enter a valid integer for the password length.")
main()