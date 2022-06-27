# "C:\py venv\kivy_venv\scripts\activate"

from kivy.app import App
#from kivy.uix.widget import Widget # untuk penggunaan regular
from kivy.uix.tabbedpanel import TabbedPanel # untuk penggunaan panel tab
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.lang import Builder
import time
from kivy.clock import Clock

# set window size
Window.size = (500, 500)

# load kv design file
Builder.load_file('basic_widgets.kv')

class MyGridLayout(TabbedPanel):
    # mendefinisikan kivy variable dari python
    # untuk merubah valuenya sertakan self.
    # untuk memanggil dari kv file, gunakan root. / app.
    #my_text = StringProperty('zakky')
    #my_progress = NumericProperty(0)
    #my_object = ObjectProperty()
    
    def __init__(self, **kwargs):
        # wajib memakai super function
        # sama saja membuat variable dalam parent class (MyGridLayout) di kivy file
        super(MyGridLayout, self).__init__(**kwargs)
        self.checked = []
    
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

    def checkbox_click(self, instance, value, string): # ( self, instance, value adalah parameter utama )
        if value == True:
            self.checked.append(string)
            self.ids.cb_label_output.text = f'string: {self.checked}'
        else:
            self.checked.remove(string)
            self.ids.cb_label_output.text = f'string: {self.checked}'

    def submit_press(self):
        get_input_text = self.ids.basic_textinput.text
        self.ids.basic_label.text = get_input_text

    def slider_slided(self, *args):
        # args berisikan list, ambil index 1 untuk mengambil value(int)
        value = str(int(args[1]))
        self.ids.slider_label.text = f'font size: {value}'
        self.ids.slider_label.font_size = int(value)

    def spinner_clicked(self, value):
        self.ids.spinner_label.text = f'you picked: {value}'

    def animate_widget(self, widget, *args): # (self, widget adalah parameter utama)
        # (widget adalah instance self dari pemanggil)
        # (bisa menghilangkan instance dengan menggantinya dengan id widget)

        animate = Animation(
            size_hint = (.9,.9),
            pos_hint = {'center_x': .5},
            font_size = 27,
            duration = .025
            )
        # (satu animate bisa terdiri beberapa element seperti size_hint, background_color dll)
        # (parameter t untuk transition, lihat di dokumentasi kivy)

        # membuat animasi ke dua
        # (bisa menggunakan &= untuk membuat animasi secara bersamaan)
        animate += Animation(
            size_hint = (1,1),
            pos_hint = {'center_x': .5},
            font_size = 30,
            duration = .05)

        # mulai animasikan
        animate.start(widget)

    def change_label_animate(self):
        self.ids.animate_stuff_label.text = 'look at that!!,\nthe button have a animation'

    def switch_click(self, switchObject, switchValue): # switchObject, switchValue are main parameter
        # switchValue me return False dan True
        if switchValue == True:
            self.ids.switch_label.text = 'ON :D'
            self.ids.switch_label.color = r'#F8FF00'
        else:
            self.ids.switch_label.color = (1,1,1,.5)
            self.ids.switch_label.text = 'OFF :('

class WidgetBasic(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    WidgetBasic().run()
