"""
CP1404 Prac 7 - My Guitars
"""

from guitar import Guitar
import csv

FILENAME = "guitars.csv"


def main():
    """Load a list of guitar objects from a CSV file, create new ones, and write them all to the file."""
    guitars = []
    read_file(guitars)
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ")

    guitars.sort()
    write_file(guitars)


def read_file(guitars):
    """Read a CSV file and append guitar objects to a list."""
    with open(FILENAME, "r") as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            row[1] = int(row[1])
            row[2] = float(row[2])
            print(row)
            guitar = Guitar(row[0], row[1], row[2])
            guitars.append(guitar)


def write_file(guitars):
    """Write the list of guitar objects to the CSV file."""
    with open(FILENAME, "w", newline="") as out_file:
        writer = csv.writer(out_file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


main()
