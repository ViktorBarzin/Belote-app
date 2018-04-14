from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from ui.homescreen import HomeScreen, BeloteGameScreen, MainSection

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


