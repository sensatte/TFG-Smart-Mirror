from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.graphics import Color, Rectangle, BorderImage
from kivy.uix.button import Button

from kivy.lang import Builder


class MenuLayout(FloatLayout):
    #import from external .kv
    Builder.load_file('menu\menu.kv')
    def __init__(self, **kwargs):
        super(MenuLayout, self).__init__(**kwargs)

        #Keyboard Handling for menuing
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)


        #Menu Background
        #with self.canvas.before:

            #Color(1, 1, 1, 0.5)        
            #Color(1, 0, 0, 1) # (R, G, B, A) ; colors range from 0-1 instead of 0-255
            #self.rect = Rectangle(size=self.size, pos=self.pos)

        #def update_rect(instance, value):
            #instance.rect.pos = instance.pos
            #instance.rect.size = instance.size

        #self.bind(pos=update_rect, size=update_rect)


        #Menu properties
        self.pos_hint={'center_y': 0, 'center_x': 0.5}
        self.size_hint=0.2,0.2
        self.opacity = 0


        #Menu contents
        #TODO Meterlos en un array o algo
        #TODO Que se autocalculen las posiciones, o convertirlo en un BoxLayout o GridLayout or something iduno
        #TODO Lógica para elegir uno de ellos y destacarlos, animandolo para que sea bigger que el resto o algo
        self.test1 = Image (source="images/icons/weather_medmin/01.png")
        self.test2 = Image (source="images/icons/weather_medmin/02.png")
        self.test3 = Image (source="images/icons/weather_medmin/03.png")
        self.test4 = Image (source="images/icons/weather_medmin/04.png")
        self.test5 = Image (source="images/icons/weather_medmin/05.png")
        self.test6 = Image (source="images/icons/weather_medmin/06.png")
        self.test7 = Image (source="images/icons/weather_medmin/07.png")
        self.test8 = Image (source="images/icons/weather_medmin/08.png")
        self.test9 = Image (source="images/icons/weather_medmin/08.png")


        self.test1.size_hint =(.1, .1)
        self.test2.size_hint =(.1, .1)
        self.test3.size_hint =(.1, .1)
        self.test4.size_hint =(.1, .1)
        self.test5.size_hint =(.1, .1)
        self.test6.size_hint =(.1, .1)
        self.test7.size_hint =(.1, .1)
        self.test8.size_hint =(.1, .1)
        self.test9.size_hint =(.1, .1)


        self.test1.pos_hint={'center_y': 0.15, 'center_x': 0.15}
        self.test2.pos_hint={'center_y': 0.15, 'center_x': 0.50}
        self.test3.pos_hint={'center_y': 0.15, 'center_x': 0.85}
        self.test4.pos_hint={'center_y': 0.50, 'center_x': 0.15}
        self.test5.pos_hint={'center_y': 0.50, 'center_x': 0.50}
        self.test6.pos_hint={'center_y': 0.50, 'center_x': 0.85}
        self.test7.pos_hint={'center_y': 0.85, 'center_x': 0.15}
        self.test8.pos_hint={'center_y': 0.85, 'center_x': 0.50}
        self.test9.pos_hint={'center_y': 0.85, 'center_x': 0.85}

        self.add_widget(self.test1)
        self.add_widget(self.test2)
        self.add_widget(self.test3)
        self.add_widget(self.test4)
        self.add_widget(self.test5)
        self.add_widget(self.test6)
        self.add_widget(self.test7)
        self.add_widget(self.test8)
        self.add_widget(self.test9)



    
        
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
        if keycode[1] == 'w':
            if (self.opacity == 1):
                self.fadeOut()
            else:
                self.fadeIn()
        return True