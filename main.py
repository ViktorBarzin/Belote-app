from mobile_app import MobileApp
# from kivy.app import App
# from kivy.uix.label import Label


# class MobileApp(App):
#     def build(self):
#         # screen_manager = ScreenManager()

#         # screen_manager.add_widget(HomeScreen(screen_manager, name='home_screen'))
#         # screen_manager.add_widget(BeloteGameScreen(screen_manager, name='belote_game_screen'))


#         # screen_manager.current = 'home_screen'
#         # # screen_manager.current = 'belote_game_screen'
#         # return screen_manager
#         return Label(text='Heelo world')


def main():
    MobileApp().run()


if __name__ == "__main__":
    main()
