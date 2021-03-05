from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.app import App
import customWidgets.NotesWidget as NotesWidget
import kivy.properties as Properties
import db.dbWrapper as dbWrapper



class ImageButton(ButtonBehavior, Image):
    note = Properties.NumericProperty()
    idwidget = Properties.NumericProperty()

class Scrolling(ScrollView):
    pass

class ColoredLabel(Label):
    background_color = Properties.ListProperty((0,0,0,1))
    visible = Properties.BooleanProperty()

class ColoredLabelConfig(ButtonBehavior, Label):
    noteid = Properties.NumericProperty()
    pinned = Properties.BooleanProperty()
    background_color = Properties.ListProperty((0,0,0,1))
    

    def pinNote(self, noteId, pinned,): 
        ColoredLabel.visible = pinned!=True
        self.pinned = pinned!=True
        note = dbWrapper.findNoteById(noteId)
        note.pinned = pinned!=True
        
        note.save()

