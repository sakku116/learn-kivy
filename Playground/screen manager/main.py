# "C:\py_venv\kivy_venv\scripts\activate"
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

import kivy
kivy.require('2.0.0')

class First(Screen):
    pass

class Second(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        kv = Builder.load_file('gui.kv')
        return WindowManager()

if __name__ == '__main__':
    MyApp().run()
