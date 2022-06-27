# "C:\py_venv\kivy_venv\scripts\activate"
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.lang import Builder

Builder.load_file('gui.kv')
class Main(Widget):
    pass

class MyApp(App):
    def build(self):
        return Main()

if __name__ == '__main__':
    MyApp().run()
