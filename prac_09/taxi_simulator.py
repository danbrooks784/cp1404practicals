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
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            current_taxi = choose_taxi(taxis)
        elif choice == "D":
            fare = drive_taxi(current_taxi)
            bill += fare
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill:.2f}")
        print(MENU)
        choice = input(">>> ").upper()


def choose_taxi(taxis):
    """Choose from a list of available taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    try:
        index = int(input(">>> "))
        chosen_taxi = taxis[index]
        return chosen_taxi
    except IndexError:
        print("Invalid taxi choice")


def drive_taxi(current_taxi):
    if current_taxi:
        current_taxi.start_fare()
        distance = int(input("Drive how far? "))
        current_taxi.drive(distance)
        fare = current_taxi.get_fare()
        print(f"Your {current_taxi.name} cost you ${fare:.2f}")
        return fare
    else:
        print("You need to choose a taxi before you can drive")
        return 0


main()
