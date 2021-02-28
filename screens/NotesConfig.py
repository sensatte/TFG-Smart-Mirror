# pylint: disable=no-member
from customWidgets.utils.BehaviorUtil import ImageButton, Scrolling, ColoredLabelConfig
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.animation import Animation
from functools import partial
from kivy.uix.screenmanager import FadeTransition
import kivy.properties as Properties

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
    backg=Properties.ListProperty([1,1,1,.2])
    backgSave=Properties.ListProperty([1,1,1,.2])
    def __init__(self, **kwargs):
        super(NotesConfig, self).__init__(**kwargs)
        
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
            self.ids.showNotes.add_widget(self.showNote(note))

            # self.ids.showNotes.add_widget(ColoredLabelConfig(noteid=note._id, text=note.title + "\n" + note.text, pinned=note.pinned,
            #                                 background_color=(note.rgb[0]/255,note.rgb[1]/255,note.rgb[2]/255,note.rgb[3])))
            # self.ids.showNotes.add_widget(ImageButton(note=note._id, source="images/menu/edit.png", size_hint_y= None, size_hint= (.17, .11)))
            # self.ids.showNotes.add_widget(self.createButton(note._id, "trash"))
    
    def showNote(self, note):
        layout=GridLayout(cols=1, spacing=[0,7])
        
        layout.add_widget(ColoredLabelConfig(noteid=note._id, text=note.title + "\n" + note.text, pinned=note.pinned,
                                            background_color=(note.rgb[0]/255,note.rgb[1]/255,note.rgb[2]/255,note.rgb[3]), size_hint=(1,5)))
        botones = BoxLayout(orientation='horizontal')
        botones.add_widget(self.createButton(note._id, "edit"))
        botones.add_widget(self.createButton(note._id, "trash"))

        layout.add_widget(botones)
        return layout
    
    def writeNote(self, title, pinned, text, date, rgb):
        date=datetime.datetime.now()
        dbWrapper.saveNote(title, pinned, text, date, rgb)
        notas=dbWrapper.getAllNotes()
        nota=notas[len(notas)-1]
        print(nota)
        self.showNotes([nota])

    def createButton(self, noteid, image):
        button=ImageButton(note=noteid, source="images/menu/"+image+".png", size_hint_y= None, size_hint= (.8, .8))
        button.bind(on_press=self.deleteNote)
        return button

    def deleteNote(self, button):
        dbWrapper.deleteNoteById(button.note)

    def editNote(self, button):
        print(button.note)



