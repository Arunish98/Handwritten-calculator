from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        with self.canvas:
            Color(1,0,0,1)
            
            touch.ud['line'] = Line(points=(touch.x, touch.y))
            

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]



class MyGrid(GridLayout):
    def __init__ (self, **kwargs):
        super(MyGrid,self).__init__(**kwargs)
        self.cols = 1
        
        self.inside = GridLayout()
        self.painter = MyPaintWidget()
        self.inside.add_widget(self.painter)
        self.add_widget(self.inside)

        self.clearbtn = Button(text='Clear',  font_size=42)
        self.clearbtn.bind(on_release=self.clear_canvas)
        self.add_widget(self.clearbtn)


    def clear_canvas(self, obj):
        self.painter.canvas.clear()
        





class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ ==  "__main__":
    MyApp().run()