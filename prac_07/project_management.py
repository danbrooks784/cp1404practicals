"""
CP1404 Prac 7 - Project Management
Estimated time: 60 minutes
Actual time:
"""

import datetime
from project import Project

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project" \
       "\n- (U)pdate project\n- (Q)uit"


def main():
    """Perform operations on project objects."""
    projects = []
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            projects = load_projects()
        elif choice == "S":
            print("Save projects")
        elif choice == "D":
            print("Display projects")
        elif choice == "F":
            print("Filter projects by date")
        elif choice == "A":
            print("Add new project")
        elif choice == "U":
            print("Update project")
        else:
            print("Invalid input")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def load_projects():
    """Load project objects from a specified file."""
    projects = []
    filename = input("Filename: ")
    with open(f"{filename}.txt", "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            parts[2] = int(parts[2])
            parts[3] = float(parts[3])
            parts[4] = int(parts[4])
            project = Project(*parts)
            projects.append(project)
    return projects


main()
