from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
import customWidgets.utils.BehaviorUtil as BehaviorUtil
import db.dbWrapper as dbWrapper
from kivy.app import App
from kivy.lang import Builder
Builder.load_file('kv\\notes.kv')

class NotesWidget(GridLayout):
    #TODO textos laargos comprimir
    
    def __init__(self, **kwargs):
        super(NotesWidget, self).__init__(**kwargs)
        self.__name__="notas"
        self.size = Window.size
        porc=self.size_hint[0]
        self.pos_hint={"x":float(Window.width-(self.width)*porc)/Window.width,"y":float(Window.height-(self.height*porc))/Window.height}
            
        showNotes(self)


        
def showNotes(self):
    noteList=dbWrapper.getAllNotes()
    num=0        
    for note in noteList:
        if(num<9 and note.pinned == True):            
            num+=1                
            self.add_widget(BehaviorUtil.ColoredLabel(visible=note.pinned, text=note.title + "\n" + note.text, #size_hint_x=None, width=100,
                                            background_color=(note.rgb[0]/255,note.rgb[1]/255,note.rgb[2]/255,note.rgb[3])))


def deleteNotes(self):
    self.remove_widget(self.children)
    self.showNotes()