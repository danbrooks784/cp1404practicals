"""
CP1404 Prac 8 - Dynamic Labels
Estimated time: 30 minutes
Actual time: 15 minutes
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabels(App):
    def __init__(self):
        """Construct class with names list."""
        super().__init__()
        self.names = ["Daniel", "James", "Emma", "Henry", "Charlotte", "Lucas"]

    def build(self):
        """Build the GUI and call function to create labels."""
        self.title = "Dynamic Labels Exercise"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create a label for every name."""
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)


DynamicLabels().run()
