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
            # TODO: Datetime shenanigans
            print("Filter projects by date")
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
    with open(f"{filename}.txt", "r") as in_file:
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
    with open(f"{filename}.txt", "w") as out_file:
        out_file.write("Name	Start Date	Priority	Cost Estimate	Completion Percentage\n")
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t"
                           f"{project.completion_percentage}\n")


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


def add_project(projects):
    """Add a new project."""
    # TODO: Add error checking
    print("Let's add a new project")
    name = input("Name: ")
    start_date = get_valid_date("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost Estimate: $"))
    completion_percentage = int(input("Completion Percentage: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects


def update_project(projects):
    """Update an existing project's completion percentage and/or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    index = int(input("Project choice: "))
    print(projects[index])
    projects[index].completion_percentage = get_valid_attribute("Percentage")
    projects[index].priority = get_valid_attribute("Priority")


def get_valid_date(message):
    """Get a valid date input in either dd/mm/yy or dd/mm/yyyy format."""
    date_string = input(message)
    is_valid_input = False
    while not is_valid_input:
        try:  # Check if format is dd/mm/yy
            date = datetime.datetime.strptime(date_string, "%d/%m/%y").date()
            is_valid_input = True
        except ValueError:
            try:  # Check if format is dd/mm/yyyy
                date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
                is_valid_input = True
            except ValueError:
                date_string = input(message)
    return date


def get_valid_attribute(attribute_name):
    """Get a valid project attribute."""
    attribute = input(f"New {attribute_name}: ")
    if attribute != "":
        is_valid_input = False
        while not is_valid_input:
            try:
                int(attribute)
                is_valid_input = True
            except ValueError:
                print("Invalid attribute.")
        return int(attribute)


main()
