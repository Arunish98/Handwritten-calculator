from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color,Rectangle

class applayout(Widget):
    pass



class tempApp(App):
    def build(self):
        return applayout()

if __name__ == "__main__":
    tempApp().run()