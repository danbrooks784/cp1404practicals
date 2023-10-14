"""
CP1404 Prac 5 - Emails
Estimate: 15 minutes
Actual: 21 minutes
"""


def main():
    """Store user emails and names in a dictionary."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        email_to_name[email] = confirm_name(name)
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    """Extract the user's name from provided email."""
    email_parts = email.split('@')
    name_parts = email_parts[0].split('.')
    name = ' '.join(name_parts)
    return name.title()


def confirm_name(name):
    """Confirm if a user's name is correct and ask for another input if not."""
    choice = input(f"Is your name {name}? (Y/n) ").upper()
    if choice != "Y" and choice != "":
        name = input("Name: ")
    return name


main()
