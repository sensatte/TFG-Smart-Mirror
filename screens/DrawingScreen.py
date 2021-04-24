from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from mongoengine.base.fields import ObjectIdField
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
from datetime import datetime
from pathlib import Path
from db import dbWrapper

#import kv
from kivy.lang import Builder
Builder.load_file('kv\\drawingScreen.kv')


class DrawingScreen(Screen):
    # TODO poner bonitos los botones grosorcito y colorcito

    ruedaOut = Properties.BooleanProperty(False)
    grosorOut = Properties.BooleanProperty(False)
    colorPincel = Properties.ListProperty((.4, 1, 1))
    grosorLinea = Properties.NumericProperty(10)

    def on_colorPincel(self, instance, value):
        self.ids.painter.colorLinea = value

    def on_grosorLinea(self, instance, value):
        self.ids.painter.grosorLinea = value

    def __init__(self, **kwargs):
        super(DrawingScreen, self).__init__(**kwargs)

    def clearDrawing(self, obj):
        self.ids.painter.canvas.clear()

    def pressedBack(self, widget):
        anim = Animation(pos_hint={"x": .1, "y": .02}, duration=.1)
        anim += Animation(pos_hint={"x": .1, "y": .05}, duration=.1)
        anim.bind(on_complete=partial(self.goToMenuScreen))
        anim.start(widget)

    def goToMenuScreen(self, widget, selected):
        App.get_running_app().root.transition = FadeTransition(duration=.3)
        App.get_running_app().root.current = "menu"

    def on_ruedaOut(self, instance, value):
        if value:
            anim = Animation(opacity=1, duration=.3)
            anim &= Animation(
                pos_hint={'center_y': 0.5, 'center_x': 0.22}, duration=.3)
            anim &= Animation(size_hint=(0.4, 0.3), duration=.3)
            anim += Animation(
                pos_hint={'center_y': 0.5, 'center_x': 0.2}, duration=.1)
            
            anim.start(self.ids.rueda)
            self.ids.painter.disabled = True
            # self.ids.grosorcito.disabled = True

        else:
            anim = Animation(
                pos_hint={'center_y': 0.5, 'center_x': 0.22}, duration=.1)
            anim.bind(on_complete=self.animfuera)
            anim.start(self.ids.rueda)

            self.ids.painter.disabled = False
            # self.ids.grosorcito.disabled = False

    def animfuera(self, instance, value):
        anim = Animation(opacity=0, duration=.3)
        anim &= Animation(
            pos_hint={'center_y': 0.5, 'center_x': 0}, duration=.3)
        anim &= Animation(size_hint=(0.4, 0.3), duration=.3)
        anim.start(self.ids.rueda)
        
    def animfuera2(self, instance, value):
        anim = Animation(opacity=0, duration=.3)
        anim &= Animation(
            pos_hint={'center_y': 0.5, 'center_x': 1}, duration=.3)
        anim &= Animation(size_hint=(0.4, 0.3), duration=.3)
        anim.start(self.ids.grosor)

    def on_grosorOut(self, instance, value):
        if value:
            anim = Animation(opacity=1, duration=.3)
            anim &= Animation(
                pos_hint={'center_y': 0.5, 'center_x': 0.88}, duration=.3)
            anim &= Animation(size_hint=(0.4, 0.3), duration=.3)
            anim += Animation(
                pos_hint={'center_y': 0.5, 'center_x': 0.9}, duration=.1)
            
            anim.start(self.ids.grosor)
            self.ids.painter.disabled = True
            # self.ids.colorcito.disabled = True

        else:
            anim = Animation(
                pos_hint={'center_y': 0.5, 'center_x': 0.88}, duration=.1)
            anim.bind(on_complete=self.animfuera2)
            anim.start(self.ids.grosor)

            self.ids.painter.disabled = False
            # self.ids.colorcito.disabled = False

    def guardarImagen(self):
        canvas = self.ids.painter

        now = datetime.now()
        imageName = now.strftime("drawing-%d-%m-%Y-%H-%M-%S.png")

        canvas.export_to_png(imageName)

        Path("./"+imageName).rename("./images/saveScreen/"+imageName)

        # TODO QUE NO SE SETEE EL ID A "SAVE"
        dbWrapper.addNewSaveScreen(imageName)


class CanvasWidget(Widget):
    colorLinea = Properties.ListProperty((1, 0, 0))
    grosorLinea = Properties.NumericProperty(10)

    def __init__(self, **kwargs):
        super(CanvasWidget, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        if not self.disabled:
            with self.canvas:
                Color(*self.colorLinea, mode='rgb')
                d = self.grosorLinea
                w = self.grosorLinea*0.5
                Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
                touch.ud['line'] = Line(
                    points=(touch.x, touch.y), size=(d, d), width=w)

    def on_touch_move(self, touch):
        if not self.disabled:
            touch.ud['line'].points += [touch.x, touch.y]
