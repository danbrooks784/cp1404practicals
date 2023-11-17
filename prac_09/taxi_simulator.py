"""
CP1404 Prac 9 - Taxi Simulator
Estimated time: 60 minutes
Actual time:
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "Let's drive!\nq)uit, c)hoose taxi, d)rive"


def main():
    """Choose a taxi, choose the distance to drive, then display trip cost."""
    current_taxi = None
    bill = 0.0
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            current_taxi = choose_taxi()
        elif choice == "D":
            print("Drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill:.2f}")
        print(MENU)
        choice = input(">>> ").upper()


def choose_taxi():
    """Choose from a list of available taxis."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    try:
        index = int(input(">>> "))
        try:
            chosen_taxi = taxis[index]
            return chosen_taxi
        except IndexError:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid choice")


main()
