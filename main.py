from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='Hello World')

TestApp().run()

def main():
    pass


if __name__ == "__main__":
    main()

