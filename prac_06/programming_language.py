"""
CP1404 Prac 6 - Programming Language class module.
"""


class ProgrammingLanguage:
    """Programming Language object."""

    def __init__(self, typing="", reflection=True, year=0):
        """Construct a programming language."""
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return if a language is dynamic."""
        return self.typing == "Dynamic"
