# pylint: disable=no-member
from customWidgets.utils.BehaviorUtil import ColoredLabelConfig, ImageButton, Scrolling
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
    #TODO color picker
    #TODO que las anim las coja de otro archivo
    #TODO solo poder coger 9
    #TODO que el tamñao de la nota sea para que no esté encojido

    showNotes=Properties.ObjectProperty(None)
    backg=Properties.ListProperty([224, 187, 228, 1])
    ind=0
    def __init__(self, **kwargs):
        super(NotesConfig, self).__init__(**kwargs)
        self.pos_hint={'center_y': 0.5, 'center_x': 0.5}        
        self.showNotes.bind(minimum_height=self.showNotes.setter('height'))

        noteList=dbWrapper.getAllNotes()
        self.showNotesFunc(noteList)

    def goToMenuScreen(self, widget, selected):
        App.get_running_app().root.transition = FadeTransition(duration=.3)
        App.get_running_app().root.current = "menu"

    def showNotesFunc(self, noteList):
        for note in noteList:
            self.ids.showNotes.add_widget(ColoredLabelConfig(editing=False, noteid=note._id, 
                        texto=note.text, pinned=note.pinned, 
                        bcolor=(note.rgb[0]/255,note.rgb[1]/255,note.rgb[2]/255,note.rgb[3])))
            self.ind+=1
    
    def writeNote(self, pinned, text, date, rgb):
        date=datetime.datetime.now()
        dbWrapper.saveNote(pinned, text, date, rgb)
        notas=dbWrapper.getAllNotes()
        nota=notas[len(notas)-1]
        self.showNotesFunc([nota])

##################################

    def pressedBack(self, widget):
        anim = Animation(pos_hint={"center_x": .5, "y": -.03}, duration=.1)
        anim += Animation(pos_hint={"center_x": .5, "y": 0}, duration=.1)
        anim.bind(on_complete=partial(self.goToMenuScreen))
        anim.start(widget)


    def badAnim(self, boton):
        anim = Animation(backgSave=[.5,.4,.4,.2], duration=.1)
        anim += Animation(backgSave=[1,1,1,.2], duration=.1)
        # anim += Animation(pos_hint={"center_x": .1, "center_y": .7}, duration=.1)
        anim.bind(on_complete=self.goTop)
        anim.start(boton)
        if self.ids.textinput.text=="":
            anim = Animation(canvBack=[1,0,0,.4], duration=.5)
            anim += Animation(canvBack=[1,1,1,.4], duration=.9)
            anim.start(self.ids.textinput)



    def goodAnim(self, boton):
        anim = Animation(backgSave=[1,1,1,.5], duration=.1)
        anim += Animation(backgSave=[1,1,1,.2], duration=.1)
        anim.bind(on_complete=self.goTop)
        anim.bind(on_complete=self.clearInputs)   
        anim.start(boton)

    def goTop(self, boton, asd):
        anim = Animation(scroll_y = 1, duration=.15)
        # if (self.ids.titletinput.text!="" and self.ids.textinput.text!=""):
        #     anim.bind(on_complete=self.switchElegir)
        #     anim.bind(on_complete=self.clearInputs)        
        anim.start(self.ids.scrollCreateNote)


    def clearInputs(self, boton, asd):
        self.ids.textinput.text=""

    def switchElegir(self, boton, asd):
        print("a")
        self.ids.panel.switch_to(self.ids.elegir)