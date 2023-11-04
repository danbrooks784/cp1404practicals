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
        return f"{self.name}, {self.start_date}, {self.priority}, ${self.cost_estimate:.2f}, " \
               f"{self.completion_percentage}%"


if __name__ == "__main__":
    test_project = Project("Test", "20/02/2033", 9, 500, 100)
    print(test_project)
