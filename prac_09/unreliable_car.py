"""
CP1404 Prac 9 - Unreliable Car class
"""

from car import Car
from random import randint


class UnreliableCar(Car):
    """Specialised version of a Car that includes a chance for drive to work."""

    def __init__(self, name, fuel, reliability):
        """Initialise an Unreliable Car instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = randint(0, 100)
        if random_number < self.reliability:
            super().drive(distance)
        else:
            return 0
