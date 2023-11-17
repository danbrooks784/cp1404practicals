"""
CP1404 Prac 9 - Silver Service Taxi class
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that raises the price per km by the fanciness passed in."""

    def __init__(self, name, fuel, fanciness):
        """Initialise a Silver Service Taxi object."""
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness
