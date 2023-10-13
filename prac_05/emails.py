"""
CP1404 Prac 5 - Emails
Estimate: 15 minutes
Actual:
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        email_to_name[email] = extract_name(email)
        email = input("Email: ")
    print(email_to_name)


def extract_name(email):
    """Extract the user's name from provided email."""
    name = email.split('@')[0]
    name_parts = name.split('.')
    name = ' '.join(name_parts)
    return name.title()


main()
