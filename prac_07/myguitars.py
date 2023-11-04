"""
CP1404 Prac 7 - My Guitars
"""

from guitar import Guitar
import csv

with open("guitars.csv", "r") as in_file:
    guitars = []
    reader = csv.reader(in_file)
    for row in reader:
        row[1] = int(row[1])
        row[2] = float(row[2])
        print(row)
        guitar = Guitar(row[0], row[1], row[2])
        guitars.append(guitar)

# Sort guitars by oldest to newest
guitars.sort()
