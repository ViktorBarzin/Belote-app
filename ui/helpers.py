from kivy.uix.boxlayout import BoxLayout
from typing import List


class LabelContainer(BoxLayout):
    def __init__(self, widgets: List, **kwargs):
        super().__init__(**kwargs)
        for widget in widgets:
            self.add_widget(widget)

