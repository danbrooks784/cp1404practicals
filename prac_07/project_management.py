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
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            print("Load projects")
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


# def load_projects():
    # filename =

main()
