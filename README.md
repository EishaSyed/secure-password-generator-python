# Secure Password Generator (Python)

A command-line password generator developed in Python that creates secure and customizable passwords based on user preferences. The application allows users to include uppercase letters, numbers, and special characters, while ensuring password complexity requirements are met.

## Features

* Generate secure random passwords
* Customize password length
* Include uppercase letters
* Include numbers
* Include special characters
* Ensure selected character types are included
* Save generated passwords to a file
* Input validation and error handling
* Menu-driven command-line interface

## Technologies Used

* Python 3
* `random` module
* `string` module
* File handling

## Concepts Demonstrated

* Functions
* Conditional statements
* Loops
* Exception handling
* String manipulation
* Randomization
* File handling
* User input validation

## Project Structure

```text
secure-password-generator-python/
│
├── password_generator.py
├── passwords.txt
└── README.md
```

## Sample Output

```text
======= PASSWORD GENERATOR =======
1. Generate Password
2. Exit
==================================
Enter your choice: 1

Enter password length (minimum 8): 12
Include uppercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): y

===== YOUR GENERATED PASSWORD =====
Password: A7#mP9@xQ2!z
Length  : 12
===================================
```

## What I Learned

* Building command-line applications in Python
* Working with randomization and character sets
* Implementing input validation and exception handling
* Performing file operations in Python
* Designing modular and reusable functions

## How to Run

1. Install Python 3.
2. Download or clone the repository.
3. Open a terminal in the project directory.
4. Run:
```bash
python password_generator.py
```
