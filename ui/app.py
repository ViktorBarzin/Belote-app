from kivy.app import App
from kivy.uix.button import Button


class MobileApp(App):
    def build(self):
        return Button(text='Hello World')


