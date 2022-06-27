# "C:\py_venv\kivy_venv\scripts\activate"
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.behaviors import TouchRippleBehavior
from kivy.uix.image import Image
from kivy.uix.button import Button

Builder.load_file('gui.kv')

class Main(Widget):
    pass

class MyImage(TouchRippleBehavior, Image):
    def on_touch_down(self, touch):
        collide_point = self.collide_point(touch.x, touch.y)
        if collide_point:
            touch.grab(self)
            self.ripple_show(touch)
            return True
        return False

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
            self.ripple_fade()
            return True
        return False

class MyButton(TouchRippleBehavior, Button):
    def on_touch_down(self, touch):
        collide_point = self.collide_point(touch.x, touch.y)
        if collide_point:
            touch.grab(self)
            self.ripple_show(touch)
            return True
        return False

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
            self.ripple_fade()
            return True
        return False

class MyApp(App):
    def build(self):
        return Main()

if __name__ == '__main__':
    MyApp().run()