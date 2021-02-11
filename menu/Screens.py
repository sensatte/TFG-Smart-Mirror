from .MenuLayout import MenuLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.graphics import Color, Rectangle, BorderImage
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App

# Builder.load_file('kv\\screens.kv')

class Screens(ScreenManager):

    def __init__(self, **kwargs):
        super(Screens, self).__init__(**kwargs)

        # Create the screen manager
        scMenu=Screen()
        scMenu.add_widget(MenuLayout())


        self.add_widget(scMenu)
        self.add_widget(Screen(name="aceituna"))

        self.current="aceituna"
        # self.add_widget(Screen(name='settings'))


   
    # keyboard buttons

    # def _keyboard_closed(self):
    #     self._keyboard.unbind(on_key_down=self._on_keyboard_down)
    #     self._keyboard = None

    # def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
    #     if keycode[1] == 'c':
    #         if (self.opacity == 1):
    #             self.fadeOut()
    #         else:
    #             self.fadeIn()

    #     if keycode[1] == 'd':
    #         self.moveRight()
    #     if keycode[1] == 'a':
    #         self.moveLeft()
    #     if keycode[1] == 'w':
    #         self.moveUp()
    #     if keycode[1] == 's':
    #         self.moveDown()
    #     if keycode[1] == 'enter':
    #         self.openSelected()

    #     return True


    # def moveUp(self):
    #     if self.selectedItem[1] < self.maxRows - 1:
    #         self.selectedItem = (self.selectedItem[0],self.selectedItem[1]+1)
    #     else:
    #         self.selectedItem = (self.selectedItem[0],0)
    #     self.updateButtons()


    # def moveDown(self):
    #     if self.selectedItem[1] > 0:
    #         self.selectedItem = (self.selectedItem[0],self.selectedItem[1]-1)
    #     else:
    #         self.selectedItem = (self.selectedItem[0],self.maxRows -1)
    #     self.updateButtons()


    # def moveRight(self):
    #     if self.selectedItem[0] < self.maxCols - 1:
    #         self.selectedItem = (self.selectedItem[0]+1,self.selectedItem[1])
    #     else:
    #         self.selectedItem = (0,self.selectedItem[1])
    #     self.updateButtons()


    # def moveLeft(self):
    #     if self.selectedItem[0] > 0:
    #         self.selectedItem = (self.selectedItem[0]-1,self.selectedItem[1])
    #     else:
    #         self.selectedItem = (self.maxCols -1,self.selectedItem[1])
    #     self.updateButtons()
        

    # def openSelected(self):
    #     #TODO abrir menu del widget                    
    #     # #llama al método de la animación con el widget de selected item
    #     self.pressedOption(self.itemsMatrix[(self.selectedItem[0],self.selectedItem[1])])         
    #     print(self.selectedItem)
    #     print(self.itemsMatrix[(self.selectedItem[0],self.selectedItem[1])])        


    # def updateButtons(self):
    #     for col in range(0, self.maxCols):
    #         for row in range(0, self.maxRows):
    #             widget = self.itemsMatrix[(col,row)]
    #             if ((col,row) == self.selectedItem):                    
    #                 self.focusOption(widget)
    #             else:
    #                 self.unfocusOption(widget)             

