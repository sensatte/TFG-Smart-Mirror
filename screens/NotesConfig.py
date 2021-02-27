# pylint: disable=no-member
from customWidgets.utils.BehaviorUtil import ImageButton, Scrolling, ColoredLabelConfig
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.app import App
from kivy.animation import Animation
from functools import partial
from kivy.uix.screenmanager import FadeTransition

import db.dbWrapper as dbWrapper
import datetime

#import kv
from kivy.lang import Builder
Builder.load_file('kv\\notesConfig.kv')

class NotesConfig(Screen):
    #TODO hacer el kv que se pueda usar pa mas gente
    #TODO color picker
    #TODO que las anim las coja de otro archivo
    #TODO poner pestaña para crear nota
    #TODO quje no puedas enviar nota vacia
    
    def __init__(self, **kwargs):
        super(NotesConfig, self).__init__(**kwargs)
        self.backg=[0,0,0,0]
        self.pos_hint={'center_y': 0.5, 'center_x': 0.5}
        noteList=dbWrapper.getAllNotes()
        self.showNotes(noteList)

    def pressedBack(self, widget):
        anim = Animation(pos_hint={"center_x": .5, "y": -.03}, duration=.1)
        anim += Animation(pos_hint={"center_x": .5, "y": 0}, duration=.1)
        anim.bind(on_complete=partial(self.goToMenuScreen))
        anim.start(widget)

    def goToMenuScreen(self, widget, selected):
        App.get_running_app().root.transition = FadeTransition(duration=.3)
        App.get_running_app().root.current = "menu"

    def showNotes(self, noteList):
        for note in noteList:
            self.ids.showNotes.add_widget(ColoredLabelConfig(noteid=note._id, text=note.title + "\n" + note.text, pinned=note.pinned,
                                            background_color=(note.rgb[0]/255,note.rgb[1]/255,note.rgb[2]/255,note.rgb[3])))

    def writeNote(self, title, pinned, text, date, rgb):
        date=datetime.datetime.now()
        dbWrapper.saveNote(title, pinned, text, date, rgb)
