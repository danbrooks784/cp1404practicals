"""
CP1404 Prac 6 - Guitar class module
Estimated time: 5 minutes
Actual time: 7 minutes
"""


class Guitar:
    """Guitar class."""

    def __init__(self, name="", year=0, cost=0):
        """Construct a guitar object."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return all the object's values."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other):
        """Determine if the guitar is older than another guitar."""
        return self.year < other.year

    def get_age(self):
        """Find the age of the guitar (current year is 2023)."""
        return 2023 - self.year

    def is_vintage(self):
        """Check if the guitar was made more than 50 years ago."""
        return self.get_age() > 50
