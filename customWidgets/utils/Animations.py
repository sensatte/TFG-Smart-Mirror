from kivy.animation import Animation
from functools import partial
from kivy.app import App


def fadeIn(widget):
    anim = Animation(opacity=1, duration=.5)
    anim &= Animation(pos_hint={'center_y': 0.5, 'center_x': 0.5}, duration=.5)
    anim &= Animation(size_hint=(.5,.4), duration=.5)
    anim.start(widget)

def fadeOut(widget):
    anim = Animation(opacity=0, duration=.5)
    anim &= Animation(pos_hint={'center_y': 0, 'center_x': 0.5}, duration=.5)
    anim &= Animation(size_hint=(0.2,0.2), duration=.5)
    anim.start(widget)


def focusOption(widget):
    anim = Animation(opacity=1,size_hint=(0.28,0.28), duration=.1)
    anim.start(widget)

def unfocusOption(widget):
    anim = Animation(opacity=1,size_hint=(0.25,0.25), duration=.1)
    anim.start(widget)


def pressedOption(widget, func, selected):
    anim = Animation(size_hint=(0.2,0.2), duration=.1)
    anim += Animation(opacity=0,size_hint=(0.3,0.3), duration=.2)
    
    anim.bind(on_complete=partial(func, selected))
    anim += Animation(opacity=1, size_hint=(0.25,0.25), duration=.2)
    anim.start(widget)









