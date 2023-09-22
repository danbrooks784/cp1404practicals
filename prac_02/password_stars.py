"""CP1404 Prac 2 - Password Stars"""


def main():
    """Run the program."""
    password = get_password()
    print_stars(password)


def get_password():
    """Get valid password from input."""
    minimum_length = 6
    password = input("Password: ")
    while len(password) < minimum_length:
        print("Password is too short")
        password = input("Password: ")
    return password


def print_stars(password):
    """Print stars based on length of password."""
    print("*" * len(password))


main()
