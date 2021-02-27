from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from customWidgets.utils.BehaviorUtil import ColoredLabel

import db.dbWrapper as dbWrapper

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
            
        noteList=dbWrapper.getAllNotes()
        showNotes(self, noteList)


def showNotes(self, noteList):
    num=0
    for note in noteList:
        if(num<9):            
            num+=1
            self.add_widget(ColoredLabel(visible=note.pinned, disabled=True, text=note.title + "\n" + note.text, #size_hint_x=None, width=100,
                                            background_color=(note.rgb[0]/255,note.rgb[1]/255,note.rgb[2]/255,note.rgb[3])))


