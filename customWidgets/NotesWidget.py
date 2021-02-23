from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.storage.jsonstore import JsonStore
from kivy.graphics import Color, Rectangle, BorderImage
import kivy.properties as Properties
from customWidgets.utils.BehaviorUtil import ColoredLabel

import json

from kivy.lang import Builder
Builder.load_file('kv\\notes.kv')

class NotesWidget(GridLayout):
    #TODO en conf lockear maximo a 3x3
    #TODO textos laargos comprimir
    
    def __init__(self, **kwargs):
        super(NotesWidget, self).__init__(**kwargs)
        self.size = Window.size
        porc=self.size_hint[0]
        self.pos_hint={"x":float(Window.width-(self.width)*porc)/Window.width,"y":float(Window.height-(self.height*porc))/Window.height}
            
        noteList=loadNotes(self)
        showNotes(self, noteList)


def loadNotes(self):
    # read file
    with open('db/notes.json', encoding='utf-8') as myfile:
        data=myfile.read()

    # parse file
    noteList = json.loads(data)

    return noteList


def showNotes(self, noteList):
    num=0
    for note in noteList:
        if((note["pinned"]=="True" and num<9)):            
            num+=1
            self.add_widget(ColoredLabel(text=note["title"] + "\n" + note["text"], #size_hint_x=None, width=100,
                                            background_color=(float(note["r"])/255, float(note["g"])/255, float(note["b"])/255, 1)))


