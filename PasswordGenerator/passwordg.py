import random
import string

def generate_password(length):
    # Define possible characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password using random.choice to pick characters randomly
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            length = int(input("\nEnter the desired length of your password: "))
            if length <= 0:
                print("Please enter a positive integer.")
                continue
            
            password = generate_password(length)
            print(f"\nYour generated password is: {password}")
            
            break  # Exit the loop if password generation is successful
        
        except ValueError:
            print("Invalid input. Please enter a valid integer for the password length.")

# Run the main function
if __name__ == "__main__":
    main()
