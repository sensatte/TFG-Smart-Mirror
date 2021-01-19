from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.graphics import Color, Rectangle, BorderImage
from kivy.uix.button import Button

class MenuLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MenuLayout, self).__init__(**kwargs)

        self.cols=3

        for x in ('schedule', "news", "settings", "at", "clock", "schedule", "settings", "settings", "settings"):
            self.add_widget(Button(background_normal = 'images\\menu\\'+x+'.png', 
                     background_down = 'images\\menu\\settings_pressed.png', ))



        #Keyboard Handling for menuing
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

        #Menu properties
        self.pos_hint={'center_y': 0, 'center_x': 0.5}
        self.size_hint=0.2,0.2
        self.opacity = 0


    
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

    
    #

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'c':
            if (self.opacity == 1):
                self.fadeOut()
            else:
                self.fadeIn()

        if keycode[1] == 'd':
            if (self.opacity == 1):
                self.fadeOut()
            else:
                self.fadeIn()

        if keycode[1] == 'a':
            if (self.opacity == 1):
                self.fadeOut()
            else:
                self.fadeIn()

        return True