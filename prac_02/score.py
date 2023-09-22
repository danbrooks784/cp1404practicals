"""CP1404 Prac 2 - Scores"""

import random


def main():
    """Run the program."""
    score = float(input("Enter score: "))
    print(determine_result(score))
    random_score = random.randint(1, 99)
    print(determine_result(random_score))


def determine_result(score):
    """Determine the result of the given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
