"""
CP1404 Prac 6 - Programming Language class module.
"""


class ProgrammingLanguage:
    """Programming Language object."""

    def __init__(self, name="", typing="", reflection=True, year=0):
        """Construct a programming language."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return all values of the class."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Return if a language is dynamically typed."""
        return self.typing == "Dynamic"
