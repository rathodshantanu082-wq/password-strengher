# Password Strength Checker

A simple Python program that evaluates the strength of a password based on key security criteria including length, uppercase letters, lowercase letters, digits, and special characters. It provides real-time feedback and suggestions to help users create stronger passwords.

## Features

- Checks if the password is at least 8 characters long
- Verifies the presence of uppercase letters
- Verifies the presence of lowercase letters
- Checks for digits
- Checks for special characters like !@#$%^&*() etc.
- Classifies passwords into three categories: Strong, Moderate, Weak
- Provides actionable feedback to improve password strength

## How it works

The program uses regular expressions to detect character types in the password. It scores the password on five criteria and classifies the strength based on the total score:

- 5/5: Strong password
- 3-4/5: Moderate password
- Less than 3: Weak password

## Usage

1. Clone or download this repository.
2. Run the `password_checker.py` script:

