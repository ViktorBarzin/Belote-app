from typing import List
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import *
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from ui.settings import sgs7_screen_size

from score_calculator import card

from kivy.config import Config
Config.set('graphics', 'width', sgs7_screen_size['width'])
Config.set('graphics', 'height', sgs7_screen_size['height'])
# Load kivy file
# Builder.load_file('ui/main.kv')


class MobileApp(App):
    def build(self):
        return HomePage()


class HomePage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MainSection())


class MainSection(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs, spacing=10,
                         orientation='vertical',
                         # size_hint=(0.8, 1),
                         # pos_hint={'top': 1})
                         )
        self.add_widget(LabelContainer([Label(text='Card Scanner', font_size=30)], size_hint=(1, 0.25)))
        self.add_widget(LabelContainer([Label(text='Choose a game to play:', font_size=20)], size_hint_y=0.25, size_hint_max_y=50))
        self.add_widget(Button(text='Belote', size_hint=(0.5, 0.25), pos_hint={'right': 0.7}, size_hint_max_y=50))
        self.add_widget(Button(text='Poker', size_hint=(0.5, 0.25), pos_hint={'right': 0.7}, size_hint_max_y=50))

        self.add_widget(LastRow(anchor_x='center', anchor_y='bottom'))


class LastRow(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.items = BoxLayout(size_hint_max_y=50)
        self.items.add_widget(Button(text='Add game', size_hint_max_y=1))
        self.items.add_widget(Button(text='Settings'))
        self.add_widget(self.items)
        self.apply_common_styles()

    def apply_common_styles(self):
        pass
        # for widget in self.children:
        #     widget.size_hint_y = 1
        #     widget.size_hint_max_y = 80


class LabelContainer(BoxLayout):
    def __init__(self, widgets: List, **kwargs):
        super().__init__(**kwargs)
        for widget in widgets:
            self.add_widget(widget)

