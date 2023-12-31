"""
CP1404 Prac 8 - Miles to Kilometers Converter
Estimated time: 60 minutes
Actual time: 41 minutes
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

CONVERSION_RATE = 1.609


class MilesKilometersConverter(App):
    """Convert a distance in miles to kilometers."""

    def build(self):
        """Build Converter app from KV file."""
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file("convert_miles_km.kv")
        self.handle_conversion()  # Convert the default distance
        return self.root

    def handle_increment(self, amount):
        """Increase or decrease the distance by 1."""
        result = self.get_distance_miles() + amount
        self.root.ids.input_field.text = str(result)

    def handle_conversion(self):
        """Convert the distance to kilometers."""
        distance_km = self.get_distance_miles() * CONVERSION_RATE
        self.root.ids.output_label.text = str(distance_km)

    def get_distance_miles(self):
        """Perform error checking on distance input."""
        try:
            return float(self.root.ids.input_field.text)
        except ValueError:
            return 0.0


MilesKilometersConverter().run()
