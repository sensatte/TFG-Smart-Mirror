# pylint: disable=no-member
from customWidgets.utils.BehaviorUtil import ImageButton, Scrolling, ColoredLabelConfig
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.app import App
from kivy.animation import Animation
from functools import partial
from kivy.uix.screenmanager import FadeTransition

import db.dbWrapper as dbWrapper

#import kv
from kivy.lang import Builder
Builder.load_file('kv\\notesConfig.kv')

class NotesConfig(Screen):
    #TODO hacer el kv que se pueda usar pa mas gente
    #TODO color picker
    #TODO que las anim las coja de otro archivo
    #TODO poner pestaña para crear nota
    
    def __init__(self, **kwargs):
        super(NotesConfig, self).__init__(**kwargs)
        self.pos_hint={'center_y': 0.5, 'center_x': 0.5}
        noteList=dbWrapper.getAllNotes()
        print(noteList)
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
            self.ids.showNotes.add_widget(ColoredLabelConfig(text=note.title + "\n" + note.text, pinned=note.pinned,
                                            background_color=(float(note.r)/255, float(note.g)/255, float(note.b)/255, 1)))

        
