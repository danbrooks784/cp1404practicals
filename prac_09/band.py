"""
CP1404 Prac 9 - Band class
"""


class Band:
    """Band class comprised of Musicians."""

    def __init__(self, name=""):
        """Construct a Band object."""
        self.name = name
        self.members = []
