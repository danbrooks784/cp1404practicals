"""
CP1404 Prac 5 - Emails
Estimate: 15 minutes
Actual:
"""


def main():
    """Store user emails and names in a dictionary."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        choice = input(f"Is your name {name}? (Y/n) ").upper()
        if choice != "y" and choice != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    print(email_to_name)


def extract_name_from_email(email):
    """Extract the user's name from provided email."""
    name = email.split('@')
    name_parts = name[0].split('.')
    name = ' '.join(name_parts)
    return name.title()


main()
