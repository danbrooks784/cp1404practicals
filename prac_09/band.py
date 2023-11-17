"""
CP1404 Prac 9 - Band class
"""


class Band:
    """Band class comprised of Musicians."""

    def __init__(self, name=""):
        """Construct a Band object."""
        self.name = name
        self.musicians = []

    def __str__(self):
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        self.musicians.append(musician)
