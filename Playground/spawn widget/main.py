# "C:\py venv\kivy_venv\scripts\activate"
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.lang import Builder
# import uix yang dibutuhkan
from kivy.uix.label import Label

Builder.load_file('kv_design.kv')
class my(Label):
    pass

class MyLayout(Widget):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        #self.layout = self.ids.layout_to_add
    def add_widgets(self):
        layout = self.ids.layout_to_add
        # atau bisa definisikan layout dalam __init__ mwnggunakan self.
        # dan panggil juga dengan self.layout
        lbl = Label(text='hello world',
            font_size=30)
        layout.add_widget(lbl)
        layout.add_widget(my())
        
class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()