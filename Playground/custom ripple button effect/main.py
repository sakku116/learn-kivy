# "C:\py venv\kivy_venv\scripts\activate"
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.animation import Animation

Builder.load_file('kv_design.kv')

class MyLayout(Widget):
    def ripple_effect(self, widget): # widget adalah self dari widget pemanggil
        # reset size
        widget.size_effect = [0,0]
        
        my_width = int(widget.width)
        my_height = int(widget.height)

        # fit the size
        if my_width > my_height:
            my_width = my_height
        else:
            my_height = my_width

        anim = Animation(
            opacity_effect = 1,
            duration = 0.01
        )
        anim &= Animation(
            opacity_effect = 1,
            size_effect = [my_width/1.5, my_height/1.5],
            duration = 0.2
        )
        anim += Animation(
            size_effect = [my_width*(1.2), my_height*(1.2)],
            opacity_effect = 0,
            duration = 0.2
        )
        anim.start(widget)



class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()