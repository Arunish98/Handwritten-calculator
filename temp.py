from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ListProperty
import random


class Scatterwidget(BoxLayout):
    text_color = ListProperty([0,0,0,1])
    def color_change(self,*args):
        color = [random.random() for x in range(3)] + [1]
        self.text_color = color
    

class MyApp(App):
    def build(self):
        return Scatterwidget()

if __name__ == "__main__":
    MyApp().run()