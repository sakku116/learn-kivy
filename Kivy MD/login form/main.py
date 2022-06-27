# "C:\py venv\kivymd_venv\scripts\activate"

from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Window.size = (500, 500)
Builder.load_file('login_form.kv')

class MyLayout(Widget):
    def login(self):
        get_username = self.ids.username_input.text
        get_pass = self.ids.pass_input.text

        if get_username == 'sakku116' and get_pass == 'kycraft116':
            self.ids.login_header_label.text = 'you logged in'
        else:
            self.ids.login_header_label.text = 'sorry!'

class MyApp(MDApp):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()
