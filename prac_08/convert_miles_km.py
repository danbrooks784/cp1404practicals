"""
CP1404 Prac 8 - Miles to Kilometers Converter
Estimated time: 60 minutes
Actual time:
"""

from kivy.app import App
from kivy.lang import Builder


class MilesKilometersConverter(App):
    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root


MilesKilometersConverter().run()
