# "C:\py venv\kivy_venv\scripts\activate"
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.animation import Animation

Builder.load_file('kv_design.kv')

class MyLayout(Widget):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)

    def spawn_widget(self, widget):
        widget.my_top = .5
        # atau bisa menggunakan animation untuk mengubah element seperti my_top
        

class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()