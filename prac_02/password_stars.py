def main():
    password = get_password()
    print("*" * len(password))


def get_password():
    minimum_length = 6
    password = input("Password: ")
    while len(password) < minimum_length:
        print("Password is too short")
        password = input("Password: ")
    return password


main()
