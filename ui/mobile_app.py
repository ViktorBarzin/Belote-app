from kivy.app import App
# from kivy.lang import Builder
# from kivy.properties import *
# from kivy.uix.widget import Widget
# from kivy.uix.button import Button
# from kivy.uix.label import Label
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.anchorlayout import AnchorLayout
# from kivy.uix.gridlayout import GridLayout
# from settings import sgs7_screen_size
from kivy.uix.screenmanager import ScreenManager, Screen
# from mixins import ChangeScreenMixin
# from helpers import LabelContainer
from ui.homescreen import HomeScreen, BeloteGameScreen, MainSection


# from score_calculator import card

from kivy.config import Config
# Config.set('graphics', 'width', sgs7_screen_size['width'])
# Config.set('graphics', 'height', sgs7_screen_size['height'])
# Load kivy file
# Builder.load_file('ui/main.kv')


class MobileApp(App):
    def build(self):
        screen_manager = ScreenManager()

        screen_manager.add_widget(HomeScreen(screen_manager, name='home_screen'))
        screen_manager.add_widget(BeloteGameScreen(screen_manager, name='belote_game_screen'))

        screen_manager.current = 'home_screen'
        # screen_manager.current = 'belote_game_screen'
        return screen_manager

    # def add_screens(self, screen_manager: ScreenManager, screens: List[Screen]):
    #     screen_manager.add_widget(screens)


