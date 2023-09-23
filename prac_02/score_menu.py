"""CP1404 Prac 2 - Score Menu"""


MENU = """(G)et score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Run the program."""
    score = get_valid_score()
    print(MENU)
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_result(score))
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input("> ").upper()
    print("Quitting...")


def get_valid_score():
    """Get a score between 0 and 100 from user."""
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Score: "))
    return score


def determine_result(score):
    """Determine the result of the given score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    """Print stars based on value of score."""
    print("*" * score)


main()
