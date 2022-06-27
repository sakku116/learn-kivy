# "C:\py_venv\kivy_venv\scripts\activate"
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.lang import Builder

Builder.load_file('gui.kv')

class MainLayout(Widget):
    def animate_progress(self):
        global time
        time = 0

        def sum(dt):
            global time
            # membuat global var agar untuk menyimpan value diluar function

            self.ids.circular_progress.my_progress += 1

            if self.ids.circular_progress.my_progress == 360:
                time += 360
            else:
                pass

            if self.ids.circular_progress.my_progress == 360:
                self.ids.circular_progress.my_progress = 0
                color_before = self.ids.circular_progress.my_color_before
                color_progress = self.ids.circular_progress.my_color_progress
                self.ids.circular_progress.my_color_before = color_progress
                self.ids.circular_progress.my_color_progress = color_before
            else:
                pass

            if time == 360*2:
                text = 'done'
            elif time >= 360:
                text = 'wtf bro'
            else:
                text = f'{int(self.ids.circular_progress.my_progress/3.6)}%'

            self.ids.circular_progress.text = text

            # menghentikan schedule pengulangan
            if time == 360*2:
                Clock.unschedule(event)

        event = Clock.schedule_interval(sum, .01)

    def circular_progress_slider(self, *args):
        value = int(args[1])
        self.ids.circular_progress.my_progress = value
        self.ids.circular_progress.text = f'{int(value/3.6)}%'

class MyApp(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    MyApp().run()
