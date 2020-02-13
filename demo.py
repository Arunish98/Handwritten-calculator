from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout




class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        with self.canvas.before:
            Color(1,0,0,1)
            
            touch.ud['line'] = Line(points=(touch.x, touch.y),width=2)
            

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]
    
    def clear_canvas(self):
        self.canvas.clear()



class LayItOn(BoxLayout):
        pass




class DemoApp(App):
    def build(self):
        return LayItOn()

if __name__ == "__main__":
    DemoApp().run()