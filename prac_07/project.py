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


if __name__ == "__main__":
    test_project = Project("Test", "20/02/2033", 9, 500, 100)
    other_project = Project("Test2", "3", 3, 3, 90)
    print(test_project.is_complete())
    print(other_project.is_complete())
    print(test_project > other_project)
