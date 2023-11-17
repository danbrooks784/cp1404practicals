"""
CP1404 Prac 9 - Unreliable Car class
"""

from car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes a chance for drive to work."""

    def __init__(self, name, fuel, reliability):
        """Initialise an Unreliable Car instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability
