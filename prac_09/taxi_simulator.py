"""
CP1404 Prac 9 - Taxi Simulator
Estimated time: 60 minutes
Actual time: 50 minutes
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "Let's drive!\nq)uit, c)hoose taxi, d)rive"


def main():
    """Choose a taxi or enter distance to drive, then display total trip cost."""
    current_taxi = None
    bill = 0.0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            print("Taxis available:")
            display_taxis(taxis)
            current_taxi = choose_taxi(taxis)
        elif choice == "D":
            drive_taxi(current_taxi)
            bill += determine_fare(current_taxi)
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill:.2f}")
        print(MENU)
        choice = input(">>> ").upper()

    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display the list of taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Choose from a list of available taxis."""
    try:
        index = int(get_valid_number(">>> "))
        chosen_taxi = taxis[index]
        return chosen_taxi
    except IndexError:
        print("Invalid taxi choice")


def drive_taxi(current_taxi):
    """Enter a distance to drive the chosen taxi."""
    try:
        current_taxi.start_fare()
        distance = get_valid_number("Drive how far? ")
        current_taxi.drive(distance)
    except AttributeError:
        print("You need to choose a taxi before you can drive")


def determine_fare(current_taxi):
    """Determine the fare for the current taxi."""
    try:
        fare = current_taxi.get_fare()
        print(f"Your {current_taxi.name} cost you ${fare:.2f}")
        return fare
    except AttributeError:
        return 0


def get_valid_number(message):
    """Get a number >= 0 as an input."""
    is_valid_input = False
    while not is_valid_input:
        try:
            number = float(input(message))
            if number < 0:
                print("Number must be >= 0")
            else:
                is_valid_input = True
                return number
        except ValueError:
            print("Invalid number")


main()
