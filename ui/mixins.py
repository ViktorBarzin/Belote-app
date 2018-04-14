class ChangeScreenMixin:
    def change_screen(self, widget):
        # I guess it is a hacky way but should be fine as long as names are
        # consistent
        if widget._label._text == 'Belote':
            self.screen_manager.current = 'belote_game_screen'
        elif widget._label._text == 'Home':
            self.screen_manager.current = 'home_screen'

