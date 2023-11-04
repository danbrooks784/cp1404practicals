"""
CP1404 Prac 7 - Project Module
Estimated time: 60 minutes
Actual time:
"""


class Project:
    """Project object."""

    def __init__(self, name="", start_date="", priority=0, cost_estimate=0.0, completion_percentage=0):
        """Construct a Project object."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return all the object's values."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, " \
               f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """Determine if a project's priority is higher than another project's priority."""
        # Lower priority *value* means a higher priority!!
        return self.priority < other.priority

    def is_complete(self):
        """Determine if a project is 100% complete."""
        return self.completion_percentage == 100

    def update_value(self, value_type):
        """Update completion percentage and priority values based on user input."""
        new_value = input(f"New {value_type}: ")
        if new_value != "":
            if value_type == "Percentage":
                self.completion_percentage = int(new_value)
            elif value_type == "Priority":
                self.priority = int(new_value)
