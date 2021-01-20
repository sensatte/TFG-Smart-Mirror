from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.graphics import Color, Rectangle, BorderImage
from kivy.uix.button import Button

#image button
from kivy.config import Config
from kivy.app import App

#import kv
from kivy.lang import Builder

"""
class ButtonApp(App):  
         
    def build(self):  
   
        # create an image a button  
        # Adding images normal.png image as button 
        # decided its position and size  
        btn = Button(text ="Push Me !", 
                     color =(1, 0, .65, 1), 
                     background_normal = 'images\icons\weather_min\01.png', 
                     background_down ='images\icons\weather_min\02.png', 
                     size_hint = (.3, .3), 
                     pos_hint = {"x":0.35, "y":0.3} 
                   )  
      
        return btn 

root = ButtonApp()
root.run()
"""

class MenuLayout(FloatLayout):
    #import from external .kv
    Builder.load_file('menu\menu.kv')
    def __init__(self, **kwargs):
        super(MenuLayout, self).__init__(**kwargs)

        self.maxCols = 3
        self.maxRows = 3

        self.selectedItem = (0,0)

        self.itemsMatrix = {}

        self.test1 = MenuOption(imageUri="images\\menu\\settings_pressed.png", maxCols=self.maxCols, maxRows=self.maxRows, posTuple=(0,0))
        self.test2 = MenuOption(imageUri="images\\menu\\settings_pressed.png", maxCols=self.maxCols, maxRows=self.maxRows, posTuple=(1,1))
        self.test3 = MenuOption(imageUri="images\\menu\\settings_pressed.png", maxCols=self.maxCols, maxRows=self.maxRows, posTuple=(2,2))

        self.add_widget(self.test1)
        self.add_widget(self.test2)
        self.add_widget(self.test3)


        #self.itemsMatrix[self.test1.posTuple]=self.test1.



        #Keyboard Handling for menuing
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

        #Menu properties
        self.pos_hint={'center_y': 0, 'center_x': 0.5}
        self.size_hint=0.2,0.2
        self.opacity=0


        #Menu contents
        #TODO Meterlos en un array o algo
        #TODO Que se autocalculen las posiciones, o convertirlo en un BoxLayout o GridLayout or something iduno
        #TODO Lógica para elegir uno de ellos y destacarlos, animandolo para que sea bigger que el resto o algo
        #self.test1 = Image (source="images/icons/weather_medmin/01.png")
        # self.test2 = Image (source="images/icons/weather_medmin/02.png")
        # self.test3 = Image (source="images/icons/weather_medmin/03.png")
        # self.test4 = Image (source="images/icons/weather_medmin/04.png")
        # self.test5 = Image (source="images/icons/weather_medmin/05.png")
        # self.test6 = Image (source="images/icons/weather_medmin/06.png")
        # self.test7 = Image (source="images/icons/weather_medmin/07.png")
        # self.test8 = Image (source="images/icons/weather_medmin/08.png")
        # self.test9 = Image (source="images/icons/weather_medmin/08.png")


        #self.test1.size_hint =(.1, .1)
        # self.test2.size_hint =(.1, .1)
        # self.test3.size_hint =(.1, .1)
        # self.test4.size_hint =(.1, .1)
        # self.test5.size_hint =(.1, .1)
        # self.test6.size_hint =(.1, .1)
        # self.test7.size_hint =(.1, .1)
        # self.test8.size_hint =(.1, .1)
        # self.test9.size_hint =(.1, .1)


        #self.test1.pos_hint={'center_y': 0.15, 'center_x': 0.15}
        # self.test2.pos_hint={'center_y': 0.15, 'center_x': 0.50}
        # self.test3.pos_hint={'center_y': 0.15, 'center_x': 0.85}
        # self.test4.pos_hint={'center_y': 0.50, 'center_x': 0.15}
        # self.test5.pos_hint={'center_y': 0.50, 'center_x': 0.50}
        # self.test6.pos_hint={'center_y': 0.50, 'center_x': 0.85}
        # self.test7.pos_hint={'center_y': 0.85, 'center_x': 0.15}
        # self.test8.pos_hint={'center_y': 0.85, 'center_x': 0.50}
        # self.test9.pos_hint={'center_y': 0.85, 'center_x': 0.85}

        #self.add_widget(self.test1)
        # self.add_widget(self.test2)
        # self.add_widget(self.test3)
        # self.add_widget(self.test4)
        # self.add_widget(self.test5)
        # self.add_widget(self.test6)
        # self.add_widget(self.test7)
        # self.add_widget(self.test8)
        # self.add_widget(self.test9)

    def moveUp(self):
        if self.selectedItem[1] < self.maxRows - 1:
            self.selectedItem[1] += 1
        else:
            self.selectedItem[1] = 0
        self.updateButtons()

    def moveDown(self):
        if self.selectedItem[1] > 0:
            self.selectedItem[1] -= 1
        else:
            self.selectedItem = self.maxRows -1
        self.updateButtons()

    def moveRight(self):
        if self.selectedItem[0] < self.maxCols - 1:
            self.selectedItem[0] += 1
        else:
            self.selectedItem[0] = 0
        self.updateButtons()

    def moveLeft(self):
        if self.selectedItem[0] > 0:
            self.selectedItem[0] -= 1
        else:
            self.selectedItem[0] = self.maxCols -1
        self.updateButtons()

    def openSelected(self):
        #TODO
        print(self.selectedItem)

    def updateButtons(self):
        for x in range(0, self.maxCols-1):
            for y in range(0, self.maxRows-1):
                widget = self.itemsMatrix[(x,y)]
                if ((x,y) == self.selectedItem):
                    #TODO setear a 1
                    widget
                else:
                    #TODO setear a 0
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
            self.moveRight()
        if keycode[1] == 'a':
            self.moveLeft()
        if keycode[1] == 'w':
            self.moveUp()
        if keycode[1] == 's':
            self.moveDown()
        if keycode[1] == 'space':
            self.openSelected()

        return True

class MenuOption(Image):

    

    def __init__(self, posTuple, maxCols, maxRows, imageUri):
        super(MenuOption, self).__init__()
        spotsX = 2*maxCols+1
        spotsY = 2*maxRows+1
        paddingX = 1/spotsX
        paddingY = 1/spotsY

        #TODO
        self.size_hint = 0.2,0.2

       

        self.pos_hint = {'center_x': paddingX*(1+posTuple[0]+1), 'center_y':paddingY*(1+posTuple[1]+1)}
        
        print ("\n\n\n")
        print (self.pos_hint)
        print ("\n\n\n")
        
        self.source=imageUri
        self.posTuple = posTuple
