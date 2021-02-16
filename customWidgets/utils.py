from kivy.animation import Animation
from functools import partial
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

class Animations():
    def __init__(self, **kwargs):
        super(Animations, self).__init__(**kwargs)
        pass


    def fadeIn(self):
        anim = Animation(opacity=1, duration=.5)
        anim &= Animation(pos_hint={'center_y': 0.5, 'center_x': 0.5}, duration=.5)
        anim &= Animation(size_hint=(0.4,0.3), duration=.5)
        anim.start(self)

    def fadeOut(self):
        anim = Animation(opacity=0, duration=.5)
        anim &= Animation(pos_hint={'center_y': 0, 'center_x': 0.5}, duration=.5)
        anim &= Animation(size_hint=(0.2,0.2), duration=.5)
        anim.start(self)


    def focusOption(self, widget):
        anim = Animation(opacity=1,size_hint=(0.28,0.28), duration=.1)
        anim.start(widget)
    
    def unfocusOption(self, widget):
        anim = Animation(opacity=1,size_hint=(0.25,0.25), duration=.1)
        anim.start(widget)


    def pressedOption(self, widget, func, selected):
        anim = Animation(size_hint=(0.2,0.2), duration=.1)
        anim += Animation(opacity=0,size_hint=(0.3,0.3), duration=.2)
        
        anim.bind(on_complete=partial(func, selected))
        anim += Animation(opacity=1, size_hint=(0.25,0.25), duration=.2)
        anim.start(widget)

class ImageButton(ButtonBehavior, Image):
    pass









