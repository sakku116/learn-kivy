# "C:\py venv\kivymd_venv\scripts\activate"
from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('first_design.kv')

class MyLayout(Widget):
    def slider(self, *args):
        value = str(int(args[1]))
        self.ids.body_label.font_size = value

class MyApp(MDApp):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()
