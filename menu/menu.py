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

        for [x,y] in (['schedule',"1"], ["news","2"], ["settings","3"], ["at","4"], ["clock","5"],[ "schedule","6"], ["settings","7"], ["settings","8"], ["settings","9"]):
            self.add_widget(Button(id=y,background_normal = 'images\\menu\\'+x+'.png', 
                     background_down = 'images\\menu\\settings_pressed.png'))

        self.selectedItem = 1

        #Keyboard Handling for menuing
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        #self._keyboard.bind(on_key_up=self._on_keyboard_up)

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

    
    #keyboard buttons

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'c':
            if (self.opacity == 1):
                self.fadeOut()
            else:
                self.fadeIn()

        if keycode[1] == 'down':
            self.nextItem()
            print('down')

        if keycode[1] == 'up':
            self.prevItem()
            print("up")

        return True
    
    def _on_keyboard_up(self, keyboard, keycode, text, modifiers):
        pass


    #move down
    def nextItem(self):
        if self.selectedItem < len(self.get_max_widgets) - 1:
            self.selectedItem += 1
        else:
            self.selectedItem = 0
        self.view_adapter.views[self.selectedItem].selected = 1
        print(self.selectedItem)

    #move down
    def prevItem(self):     
        if self.selectedItem > 0:
            self.selectedItem -= 1
        else:
            self.selectedItem = len(self.get_max_widgets()) - 1
            print(self.get_max_widgets())
        self.view_adapter.views[self.selectedItem].selected = 1
        print(self.selectedItem)



    #ids widget
    def get_id(self,  instance):
        for id, widget in instance.parent.ids.items():
            if widget.__self__ == instance:
                return id