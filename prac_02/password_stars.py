def main():
    minimum_length = 6
    password = input("Password: ")
    while len(password) < minimum_length:
        print("Password is too short")
        password = input("Password: ")
    print("*" * len(password))


main()
