"""
CP1404 Prac 6 - Guitars
Estimated time: 15 minutes
Actual time:
"""

from guitar import Guitar


def main():
    """"""
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ")


main()
