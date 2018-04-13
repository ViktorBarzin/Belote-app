from kivy.uix.screenmanager import ScreenManager, Screen
from ui.mixins import ChangeScreenMixin
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from ui.helpers import LabelContainer
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from ui.belotescreen import BeloteGameScreen


class HomeScreen(Screen):
    def __init__(self, screen_manager: ScreenManager, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = screen_manager
        self.items = BoxLayout()
        self.items.add_widget(MainSection(self.screen_manager))
        self.add_widget(self.items)


class MainSection(ChangeScreenMixin, BoxLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs, spacing=10,
                         orientation='vertical',
                         # size_hint=(0.8, 1),
                         # pos_hint={'top': 1})
                         )
        self.screen_manager = screen_manager
        self.add_widget(LabelContainer([Label(text='Card Scanner', font_size=30)], size_hint=(1, 0.25)))
        self.add_widget(LabelContainer([Label(text='Choose a game to play:', font_size=20)], size_hint_y=0.25, size_hint_max_y=50))
        # Later on add buttons based on available games, don't hard code them
        belote_button = Button(text='Belote', size_hint=(0.5, 0.25), pos_hint={'right': 0.7}, size_hint_max_y=50)
        belote_button.bind(on_press=self.change_screen)
        self.add_widget(belote_button)
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

