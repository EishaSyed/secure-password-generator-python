import random
import string

# character sets
lowercase = string.ascii_lowercase  # a-z
uppercase = string.ascii_uppercase  # A-Z
digits = string.digits              # 0-9
symbols = string.punctuation        # !@#$%^&*...


def generate_password(length, use_uppercase, use_digits, use_symbols):
    
    # always include lowercase
    characters = lowercase
    
    # add more characters based on user choices
    if use_uppercase:
        characters += uppercase
    if use_digits:
        characters += digits
    if use_symbols:
        characters += symbols
    
    # make sure at least one character from each selected type is included
    password = []
    
    if use_uppercase:
        password.append(random.choice(uppercase))
    if use_digits:
        password.append(random.choice(digits))
    if use_symbols:
        password.append(random.choice(symbols))
    
    # fill the rest of the password randomly
    remaining = length - len(password)
    for i in range(remaining):
        password.append(random.choice(characters))
    
    # shuffle so guaranteed characters aren't always at the start
    random.shuffle(password)
    
    # join list into a string
    return "".join(password)

def save_password(password):
    with open("passwords.txt", "a") as file:
        file.write(password + "\n")
    print("Password saved to passwords.txt successfully!")


def main():
    while True:
        print("\n======= PASSWORD GENERATOR =======")
        print("1. Generate Password")
        print("2. Exit")
        print("==================================")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            # get password length
            while True:
                try:
                    length = int(input("Enter password length (minimum 8): "))
                    if length < 8:
                        print("Password must be at least 8 characters!")
                    else:
                        break
                except ValueError:
                    print("Please enter a valid number!")
            
            # get user preferences
            use_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
            use_digits = input("Include numbers? (y/n): ").lower() == "y"
            use_symbols = input("Include symbols? (y/n): ").lower() == "y"
            
            # generate password
            password = generate_password(length, use_uppercase, use_digits, use_symbols)
            
            print("\n===== YOUR GENERATED PASSWORD =====")
            print("Password: " + password)
            print("Length  : " + str(len(password)))
            print("===================================")
            
            # ask to save
            save = input("Save this password? (y/n): ").lower()
            if save == "y":
                save_password(password)
                
        elif choice == "2":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice! Try again.")

# run the program
main()