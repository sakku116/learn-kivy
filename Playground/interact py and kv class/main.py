# "C:\py venv\kivy_venv\scripts\activate"
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.animation import Animation

Builder.load_file('main.kv')

class MyWidget(Button):
    text = 'sakku'
    background_normal = ''
    # attribute elemen default pada parent class bisa langsung dibuat variable dalam python
    # asalkan variable dalam python sama dengan nama attribute sebuah widget dalam kivy

    def animate(self):
        anim = Animation(background_color = (0,0,0,1))
        anim.start(self)

class MyLayout(Widget):
    t = StringProperty('zakky')
    t2 = 'zakky'

class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()
