"""
CP1404 Prac 9 - Silver Service Taxi class
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that raises the price per km by the fanciness passed in."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a Silver Service Taxi object."""
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return a string like a Taxi but with the flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the taxi trip with the flagfall."""
        return self.flagfall + super().get_fare()
