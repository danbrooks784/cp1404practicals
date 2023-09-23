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
            score = get_valid_score()
        elif choice == "P":
            pass
        elif choice == "S":
            pass
        else:
            print("Invalid choice.")
            print(MENU)
            choice = input("> ").upper()


def get_valid_score():
    """Get a score between 0 and 100 from user."""
    score = int(input("Score: "))
    while score <= 0 or score >= 100:
        print("Invalid score")
        score = int(input("Score: "))
    return score


main()
