"""
CP1404 Prac 3 - Password Checker
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # Check if the password meets the minimum and maximum length requirements
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    # Determine the type of every character in the password
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isdigit():
            count_digit += 1
        elif char in SPECIAL_CHARACTERS:
            count_special += 1

    # Check if there is one of each "normal" character in the password
    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False

    # Check if there is a special character in the password, if special characters are required
    if SPECIAL_CHARS_REQUIRED and count_special == 0:
        return False

    # If the function reaches this stage, the password is valid
    return True


main()
