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
            projects = load_projects()
        elif choice == "S":  # Save projects
            save_projects(projects)
        elif choice == "D":  # Display projects
            projects.sort()
            display_projects(projects)
        elif choice == "F":  # Filter projects
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
    name = input("Name: ")
    start_date = input("Start Date: ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost Estimate: $"))
    completion_percentage = int(input("Completion Percentage: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects


def update_project(projects):
    """Update an existing project's completion percentage and/or priority."""
    # TODO: Add error checking
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    print(projects[choice])
    projects[choice].update_value("Percentage")
    projects[choice].update_value("Priority")


main()
