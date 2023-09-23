"""CP1404 Prac 2 - Score Menu"""


MENU = """(G)et score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Run the program."""
    print(MENU)
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "G":
            pass
        elif choice == "P":
            pass
        elif choice == "S":
            pass
        else:
            print("Invalid choice.")
            print(MENU)
            choice = input("> ").upper()


main()
