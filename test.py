from kivy.app import App
from kivy.properties import StringProperty
from kivy.lang import Builder
from customWidgets.utils.BehaviorUtil import DraggableBaseWidget
from kivy.core.window import Window

KV = """

#:import win kivy.core.window

<DraggableBaseWidget>:
    canvas.before:
        Color:
            rgba: 0.2,0.5,0.4,1
        Rectangle:
            pos: 0, 0
            size: self.size

FloatLayout:
    DraggableBaseWidget:
        size_hint: .3, .3

        Image:
            size: self.parent.size
            source: "images/imageFile.jpeg"

    DraggableBaseWidget:
        size_hint: .3, .3
        pos: 50, 50

        Label:
            text:"Esto es un test"

"""

Window.size = (540, 700)
# Window.size = (540, 960)
Window.minimum_width, Window.minimum_height = Window.size


class MyApp(App):

    def build(self):
        return Builder.load_string(KV)


MyApp().run()
