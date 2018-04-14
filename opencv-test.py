import kivy
from kivy.app import App
from kivy.uix.label import Label
import numpy
import cv2


class MyApp(App):
    def build(self):
        print('eho')
        return Label(text='Hello world Numpy '+numpy.__version__+' Opencv '+cv2.__version__)

# if __name__ == 'main':
MyApp().run()

