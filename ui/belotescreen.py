from ui.mixins import ChangeScreenMixin
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class BeloteGameScreen(ChangeScreenMixin, Screen):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = screen_manager
        self.items = BoxLayout(orientation='vertical')

        home_screen_btn = Button(text='Home')
        home_screen_btn.bind(on_press=self.change_screen)
        self.items.add_widget(home_screen_btn)
        # camera_widget = Camera(play=True, resolution=(640, 480))
        # self.items.add_widget(camera_widget)
        # button = Button(text='Take Picture', size_hint=(0.12, 0.12))
        # # button.bind(on_press=self.capture)
        # self.items.add_widget(button)
        self.add_widget(self.items)


