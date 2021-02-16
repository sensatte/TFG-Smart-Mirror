from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.uix.screenmanager import FadeTransition
from kivy.uix.screenmanager import CardTransition
from kivy.app import App

#import kv
from kivy.lang import Builder
Builder.load_file('kv\\menu.kv')

class MenuLayout(FloatLayout):
    
    def __init__(self, **kwargs):
        super(MenuLayout, self).__init__(**kwargs)

        self.maxCols = 3
        self.maxRows = 3

        self.activated=False

        self.selectedItem = (0,2)      
        #TODO oscurecer fondo al abrir menu
        #TODO que no escuche al teclado si no está menu
        #TODO poner teclado en .py distinto
        #TODO otra forma de llamar a las pantallas que no sea el switch este feo
                 
        widgetList=['schedule', "news", "settings", "at", "clock", "schedule", "settings", "settings", "settings"]

        ind=0
        self.itemsMatrix = {}

        for i in range(self.maxCols):
            for j in range(self.maxRows):
                self.itemsMatrix[(i,j)]= MenuOption(name= widgetList[ind], imageUri="images\\menu\\" + widgetList[ind] + ".png", maxCols=self.maxCols, maxRows=self.maxRows, posTuple=(i,j))
                ind+=1
        
        for widget in self.itemsMatrix.values():
            self.add_widget(widget)

        self.updateButtons() #Para que empiece focuseado el widget

        #TODO populatedmenu

        #Keyboard Handling for menuing
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

        #Menu properties
        self.pos_hint={'center_y': 0, 'center_x': 0.5}
        self.size_hint=0.2,0.2 #valor inicial
        self.opacity=0

        
    # animations

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

    def pressedOption(self, widget):
        anim = Animation(size_hint=(0.2,0.2), duration=.1)
        anim += Animation(opacity=0,size_hint=(0.3,0.3), duration=.2)
        anim.start(widget)


    
    # keyboard buttons

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'c':
            if (self.activated==True):
                self.activated==False
                self.fadeOut()
                App.get_running_app().root.transition = CardTransition(duration=1)
                App.get_running_app().root.current = "home"
                
            else:
                self.activated==True
                self.fadeIn()
                App.get_running_app().root.transition = FadeTransition(duration=.3)
                App.get_running_app().root.current = "menu"

        if keycode[1] == 'd':
            self.moveRight()
        if keycode[1] == 'a':
            self.moveLeft()
        if keycode[1] == 'w':
            self.moveUp()
        if keycode[1] == 's':
            self.moveDown()
        if keycode[1] == 'enter':
            self.openSelected()

        return True


    def moveUp(self):
        if self.selectedItem[1] < self.maxRows - 1:
            self.selectedItem = (self.selectedItem[0],self.selectedItem[1]+1)
        else:
            self.selectedItem = (self.selectedItem[0],0)
        self.updateButtons()


    def moveDown(self):
        if self.selectedItem[1] > 0:
            self.selectedItem = (self.selectedItem[0],self.selectedItem[1]-1)
        else:
            self.selectedItem = (self.selectedItem[0],self.maxRows -1)
        self.updateButtons()


    def moveRight(self):
        if self.selectedItem[0] < self.maxCols - 1:
            self.selectedItem = (self.selectedItem[0]+1,self.selectedItem[1])
        else:
            self.selectedItem = (0,self.selectedItem[1])
        self.updateButtons()


    def moveLeft(self):
        if self.selectedItem[0] > 0:
            self.selectedItem = (self.selectedItem[0]-1,self.selectedItem[1])
        else:
            self.selectedItem = (self.maxCols -1,self.selectedItem[1])
        self.updateButtons()
        

    def openSelected(self):
        #TODO abrir menu del widget                    
        # #llama al método de la animación con el widget de selected item
        self.pressedOption(self.itemsMatrix[(self.selectedItem[0],self.selectedItem[1])])
        App.get_running_app().root.transition = FadeTransition(duration=.3)
        App.get_running_app().root.current = self.itemsMatrix.get(self.selectedItem).name


    def updateButtons(self):
        for col in range(0, self.maxCols):
            for row in range(0, self.maxRows):
                widget = self.itemsMatrix[(col,row)]
                if ((col,row) == self.selectedItem):                    
                    self.focusOption(widget)
                else:
                    self.unfocusOption(widget)             


class MenuOption(Image):    

    def __init__(self, name, posTuple, maxCols, maxRows, imageUri):
        super(MenuOption, self).__init__()

        #Posiciones widgets
        self.size_hint = 0.25,0.25
        self.name = name
        self.focus=True
        c = 1/maxCols
        r = 1/maxRows
    
        self.pos_hint = {'center_x': c * (posTuple[0])+c/2, 'center_y': r * (posTuple[1])+r/2}
        
        self.source=imageUri
        self.posTuple = posTuple
