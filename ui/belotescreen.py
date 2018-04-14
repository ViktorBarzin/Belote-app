from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
import os
from kivy.uix.button import Button
from kivy.uix.camera import Camera
from kivy.uix.screenmanager import ScreenManager, Screen
from os.path import exists
from plyer import camera
from plyer import notification
from settings import IMAGE_NAME
from ui.mixins import ChangeScreenMixin
# from card_recognition import CardDetector


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
        # # TODO: Hardcodes for android !!!
        # from jnius import autoclass
        # print(autoclass('org.kivy.android.PythonActivity').mActivity.getExternalCacheDir().getPath())
        # print(os.path.join(App.get_running_app().user_data_dir, IMAGE_NAME))
        # picture = camera.take_picture(autoclass('org.kivy.android.PythonActivity').mActivity.getExternalCacheDir().getPath() + '/' + IMAGE_NAME, on_complete=self.camera_callback)
        # Saves to /sdcard/mobile/capture.jpg  (if lucky)
        camera.take_picture(os.path.join(App.get_running_app().user_data_dir, IMAGE_NAME), on_complete=self.camera_callback)
        # notification.notify('in do_capture', 'sled')

    def camera_callback(self, filepath):
        # print('C' * 40 + str(filepath))
        if(exists(filepath)):
            notification.notify('callback', filepath)
        #     popup = MsgPopup("Picture saved!")
        #     popup.open()
        else:
            notification.notify('callback', 'nope')
        #     popup = MsgPopup("Could not save your picture!")
        #     popup.open()
        # return True
        # CardDetector.main(filepath)
        # return False


class MyCamera(Camera):
    def on_load(self):
        print('aaa')
