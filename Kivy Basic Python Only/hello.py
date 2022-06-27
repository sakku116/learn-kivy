import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# ini adalah bagaimana membuat kivy app hanya dengan python dan desain default
class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 1 # (MAIN GRID)
        self.row_force_default=True
        self.row_default_height=100
        self.col_force_default=True
        self.col_default_width=50
        # kivy tidak bisa membuat columnspan, bisa menggunakan trik lain
        # buat grid lagi dengan jumlah column yang ditentukan

        # (SUB GRID) deklarasikan sub grid
        self.top_grid = GridLayout(row_force_default=True,
            row_default_height=40,
            col_force_default=True,
            col_default_width=100) # (untuk mengatur ukuran per grid/layout (keseluruhan))
        self.top_grid.cols = 2

        self.label_name = Label(text='name:') # (Label/TextInput untuk mendeklarasikan widget)
        self.input_name = TextInput(multiline=True) 
        self.label_fav = Label(text='favorite pizza:')
        self.input_pizza = TextInput(multiline=False)
        self.button_submit = Button(text="submit")
            #font_size=32,
            #size_hint_y=None,
            #height=50,
            #size_hint_x=None,
            #width=200) # (ini untuk mengatur ukuran per widget)
        # bind the submit button to function
        self.button_submit.bind(on_press=self.button_pressed)

        self.top_grid.add_widget(self.label_name) # (add_widget untuk menampilkan widget)
        self.top_grid.add_widget(self.input_name) 
        self.top_grid.add_widget(self.label_fav)
        self.top_grid.add_widget(self.input_pizza)
        # (widget diatas harus ditempatkan pada top grid dengan menambahkan top_grid sebelum add_widget)
        self.add_widget(self.top_grid) # (layaknya widget, sub grid juga ditampilkan sebagai widget ke main grid)
        self.add_widget(self.button_submit) # berbeda dengan diatas, button akan ditampilkan di main grid untuk membentuk columnspan
        
    def button_pressed(self, instance):
        name = self.input_name.text# untuk mendapat input teks, hanya perlu memanggil variable widget textInput
        pizza = self.input_pizza.text # tambahkan .text untuk alias TextInput
        #print(f'hello{name}, you like {pizza} pizza')

        # print the text to the app
        self.add_widget(Label(text=f'hello {name}, you like {pizza} pizza'))
        
        # clear input boxes
        self.input_name.text = ""
        self.input_pizza.text = ""
        #.text layaknya configurator terhadap widget text input yang sudah ada


# main APP / build the window
class MyApp(App):
    def build(self):
        return MyGridLayout()

# i dont know this works but this code is to run the kivy app
if __name__ == '__main__':
    MyApp().run()

