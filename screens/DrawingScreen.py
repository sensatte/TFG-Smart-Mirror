from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from customWidgets.utils.BehaviorUtil import ImageButton
from kivy.clock import Clock

from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.animation import Animation
from functools import partial
from kivy.uix.screenmanager import FadeTransition
from kivy.uix.colorpicker import ColorWheel
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.dropdown import DropDown
import kivy.properties as Properties

#import kv
from kivy.lang import Builder
Builder.load_file('kv\\drawingScreen.kv')

class DrawingScreen(Screen):
    #TODO primera vez que pula sale negro

    #TODO que lo que dibuejs puedas guardarlo para luego verlo en una galeria (la que muestre los salvapantallas?))

    # colorPincel = Properties.ListProperty([1,0,0,1])

    def __init__(self, **kwargs):
        super(DrawingScreen, self).__init__(**kwargs)
        # self.add_widget(Frame())

    def clearDrawing(self, obj):
        self.ids.painter.canvas.clear()

    def pressedBack(self, widget):
        anim = Animation(pos_hint={"center_x": .5, "y": -.03}, duration=.1)
        anim += Animation(pos_hint={"center_x": .5, "y": 0}, duration=.1)
        anim.bind(on_complete=partial(self.goToMenuScreen))
        anim.start(widget)

    def goToMenuScreen(self, widget, selected):
        App.get_running_app().root.transition = FadeTransition(duration=.3)
        App.get_running_app().root.current = "menu"

    def showColorWheel(self):
        if self.ids.rueda.center_y==0:
            anim = Animation(opacity=1, duration=.5)
            anim &= Animation(pos_hint={'center_y': 0.5, 'center_x': 0.5}, duration=.5)
            anim &= Animation(size_hint=(0.4,0.3), duration=.5)
            anim.start(self.ids.rueda)
            self.ids.painter.disabled=True
        else:
            anim = Animation(opacity=0, duration=.5)
            anim &= Animation(pos_hint={'center_y': 0, 'center_x': 0.5}, duration=.5)
            anim &= Animation(size_hint=(0.2,0.2), duration=.5)
            anim.start(self.ids.rueda)
            
            self.ids.painter.disabled=False
            self.ids.painter.color = self.ids.rueda.colorPincel


class MyPaintWidget(Widget):
    colora = Properties.ListProperty((.4,1,1))
    def __init__(self, **kwargs):
        super(MyPaintWidget, self).__init__(**kwargs)
        Clock.schedule_once(self.on_start)

    def on_start(self, *args):
        self.colora=DrawingScreen().ids.rueda.colorPincel

    def on_touch_down(self, touch):
        # color = (random(), 1, 1)
        self.colora=DrawingScreen().ids.rueda.colorPincel
        with self.canvas:
            Color(*self.colora, mode='rgb')
            d = 10.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y), size=(d, d), width=4)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

    def showColorWheel(self):
        if self.ids.rueda.center_y==0:
            anim = Animation(opacity=1, duration=.5)
            anim &= Animation(pos_hint={'center_y': 0.5, 'center_x': 0.5}, duration=.5)
            anim &= Animation(size_hint=(0.4,0.3), duration=.5)
            anim.start(self.ids.rueda)
            self.ids.painter.disabled=True
        else:
            anim = Animation(opacity=0, duration=.5)
            anim &= Animation(pos_hint={'center_y': 0, 'center_x': 0.5}, duration=.5)
            anim &= Animation(size_hint=(0.2,0.2), duration=.5)
            anim.start(self.ids.rueda)
            
            self.ids.painter.disabled=False
            self.ids.painter.color = self.ids.rueda.colorPincel


# class AutonomousColorWheel(ColorWheel):
#     def __init__(self, **kwarg):
#         super(AutonomousColorWheel, self).__init__(**kwarg)
#         self.init_wheel(dt = 0) 

#     def on__hsv(self, instance, value):
#         super(AutonomousColorWheel, self).on__hsv(instance, value)
#         print(instance.hsv)     #Or any method you want to trigger


class CustomColorWheel(ColorWheel):
    def __init__(self, **kwargs):
        super(CustomColorWheel, self).__init__(**kwargs)
        self.register_event_type('on_press')
        self.register_event_type('on_release')

    def on_touch_down(self, touch):
        res = super(CustomColorWheel, self).on_touch_down(touch)
        if res is None:
            self.dispatch('on_press')
        return res

    def on_touch_up(self, touch):
        super(CustomColorWheel, self).on_touch_up(touch)
        if self.collide_point(*touch.pos) and touch.grab_current is self:
            self.dispatch('on_release')
            return True

    def on_press(self):
        pass

    def on_release(self):
        pass

class Frame(FloatLayout):
    def update(self):
        color = self.ids['colory']
        # DrawingScreen().ids.rueda.colorPincel=color
        print(color.color)

class CustomDropDown(FloatLayout):
    pass