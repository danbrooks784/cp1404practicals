"""
CP1404 Prac 8 - Miles to Kilometers Converter
Estimated time: 60 minutes
Actual time:
"""

from kivy.app import App
from kivy.lang import Builder

CONVERSION_RATE = 1.609


class MilesKilometersConverter(App):
    """Convert a distance in kilometers to miles."""
    def build(self):
        """Build Converter app from KV file."""
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_increment(self, amount):
        """Increase or decrease the input field by 1."""
        result = float(self.root.ids.input_field.text) + amount
        self.root.ids.input_field.text = str(result)

    def handle_conversion(self, distance_km):
        """Convert the distance to miles."""
        distance_miles = float(distance_km) * CONVERSION_RATE
        self.root.ids.output_label.text = str(distance_miles)


MilesKilometersConverter().run()
