from kivy.app import App
from kivy.uix.button import Button

from score_calculator import card


class MobileApp(App):
    def build(self):
        card.Card()
        return Button(text='Hello World')


