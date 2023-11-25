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
        """Return the Band name and every Musician in the Band."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a new Musician to the Band."""
        self.musicians.append(musician)

    def play(self):
        """Display the play method for every Musician."""
        for musician in self.musicians:
            print(musician.play())
