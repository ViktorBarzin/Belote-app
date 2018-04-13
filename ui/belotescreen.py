from ui.mixins import ChangeScreenMixin
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
# from kivy.core.camera import Camera
from os.path import exists
from plyer import camera


class BeloteGameScreen(ChangeScreenMixin, Screen):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = screen_manager
        self.items = BoxLayout(orientation='vertical')

        home_screen_btn = Button(text='Home')
        home_screen_btn.bind(on_press=self.change_screen)
        self.items.add_widget(home_screen_btn)
        # print(camera_widget.index)
        button = Button(text='Scan cards', on_press=self.do_capture)
        # button.bind(on_press=self.capture)
        self.items.add_widget(button)
        self.add_widget(self.items)

    def do_capture(self, widget):
        from plyer import notification
        notification.notify('in do_capture', 'predi')
        # picture = camera.take_picture('/Internal storage/Download/pls_work.jpg', on_complete=self.camera_callback)
        from jnius import autoclass
        print('BB'*40)
        print(autoclass('org.kivy.android.PythonActivity').mActivity.getExternalCacheDir().getPath())
        picture = camera.take_picture(autoclass('org.kivy.android.PythonActivity').mActivity.getExternalCacheDir().getPath() + '/pls.jpg', on_complete=self.camera_callback)
        notification.notify('in do_capture', 'sled')

    def camera_callback(self, filepath):
        print('B' * 40 + str(picture))
        if(exists(filepath)):
            popup = MsgPopup("Picture saved!")
            popup.open()
        else:
            popup = MsgPopup("Could not save your picture!")
            popup.open()
        return True


class MyCamera(Camera):
    def on_load(self):
        print('aaa')
