"""
CP1404 Prac 8 - Dynamic Labels
Estimated time: 30 minutes
Actual time:
"""

from kivy.app import App
from kivy.lang import Builder


class DynamicLabels(App):
    def __init__(self):
        super().__init__()
        self.names = ["Daniel", "James", "Emma", "Henry", "Charlotte", "Lucas"]

    def build(self):
        self.title = "Dynamic Labels Exercise"
        self.root = Builder.load_file("dynamic_labels.kv")
        return self.root


DynamicLabels().run()
