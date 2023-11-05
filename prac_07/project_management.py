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
        if choice == "L":  # Load projects
            load_projects(projects)
        elif choice == "S":  # Save projects
            save_projects(projects)
        elif choice == "D":  # Display projects
            projects.sort()
            display_projects(projects)
        elif choice == "F":  # Filter projects
            filter_projects(projects)
        elif choice == "A":  # Add project
            add_project(projects)
        elif choice == "U":  # Update project
            update_project(projects)
        else:
            print("Invalid input")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def load_projects(projects):
    """Load project objects from a specified file."""
    filename = input("Filename: ")
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            parts[1] = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            parts[2] = int(parts[2])
            parts[3] = float(parts[3])
            parts[4] = int(parts[4])
            project = Project(*parts)
            projects.append(project)
    return projects


def save_projects(projects):
    """Save projects to a specified file."""
    filename = input("Filename: ")
    with open(filename, "w") as out_file:
        out_file.write("Name	Start Date	Priority	Cost Estimate	Completion Percentage\n")
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                           f"{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    """Display incomplete projects, then complete projects."""
    print("Incomplete projects:")
    for project in projects:
        if not project.is_complete():
            print(f"  {project}")
    print("Complete projects:")
    for project in projects:
        if project.is_complete():
            print(f"  {project}")


def filter_projects(projects):
    """Display projects that were started after a specific date."""
    filter_date = get_valid_date("Show projects that start after date (dd/mm/yy): ")
    for project in projects:
        if project.start_date >= filter_date:
            print(project)


def add_project(projects):
    """Add a new project."""
    print("Let's add a new project")
    name = input("Name: ")  # Format: String
    start_date = get_valid_date("Start date (dd/mm/yy): ")  # Format: Datetime
    priority = get_valid_number("Priority: ", 1, 9, True)  # Format: Integer
    cost_estimate = get_valid_number("Cost Estimate: $", 0, 1000000, False)  # Format: Float
    completion_percentage = get_valid_number("Completion Percentage: ", 0, 100, True)  # Format: Integer
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects


def update_project(projects):
    """Update an existing project's completion percentage and/or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    index = int(input("Project choice: "))
    print(projects[index])
    projects[index].completion_percentage = get_valid_number("New Percentage: ", 0, 100, True)
    projects[index].priority = get_valid_number("New Priority: ", 1, 9, True)


def get_valid_number(message, low, high, is_integer):
    """Get a number that is within specified bounds."""
    is_valid_input = False
    while not is_valid_input:
        try:
            number = float(input(message))
            if low <= number <= high:
                if is_integer:
                    number = int(number)
                is_valid_input = True
            else:
                print(f"Number must be more than {low} and less than {high}.")
        except ValueError:
            print("Invalid number.")
    return number


def get_valid_date(message):
    """Get a valid date input in either dd/mm/yy or dd/mm/yyyy format."""
    is_valid_input = False
    while not is_valid_input:
        date_string = input(message)
        try:  # Check if format is dd/mm/yy
            date = datetime.datetime.strptime(date_string, "%d/%m/%y").date()
            is_valid_input = True
        except ValueError:
            try:  # Check if format is dd/mm/yyyy
                date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
                is_valid_input = True
            except ValueError:
                print("Invalid date.")
    return date


main()
