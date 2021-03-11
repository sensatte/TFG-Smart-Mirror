from db.Documents import Gifs
from kivy.uix.behaviors.togglebutton import ToggleButtonBehavior
from kivy.uix.image import AsyncImage, Image
from kivy.uix.behaviors import ButtonBehavior, DragBehavior
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.app import App
import customWidgets.NotesWidget as NotesWidget
import kivy.properties as Properties
import db.dbWrapper as dbWrapper
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.clock import Clock
from db.Documents import Notes
import logging
import datetime


class ImageButton(ButtonBehavior, Image):
    note = Properties.NumericProperty()
    gif = Properties.NumericProperty()
    idwidget = Properties.NumericProperty()


class PlayListToggle(ToggleButtonBehavior, AsyncImage):
    pass


class Scrolling(ScrollView):
    pass


class ColoredLabel(Label):
    background_color = Properties.ListProperty((0, 0, 0, 1))
    visible = Properties.BooleanProperty()


class DraggableColoredLabel(DragBehavior, Label):
    background_color = Properties.ListProperty((0, 0, 0, 1))
    visible = Properties.BooleanProperty()
    saveOnDBEvent = Properties.ObjectProperty()
    noteId = Properties.NumericProperty()

    def on_pos(self, instance, value):
        try:
            self.bringToFront()
            self.saveOnDBEvent.cancel()
        except:
            logging.info('Notes: No previous event')

        self.saveOnDBEvent = Clock.schedule_once(self.saveOnDB, 5)

    def bringToFront(self):
        parent = self.parent
        children = parent.children
        childOnTop = children[0]

        if (self != childOnTop):
            parent.remove_widget(self)
            parent.add_widget(self)

    def saveOnDB(self, dt):
        # TODO SAVE SOURCE, POS AND SIZE ON DB

        noteToSave = Notes(
            _id=self.noteId,
            pinned=self.visible,
            text=self.text,
            posX=self.pos[0],
            posY=self.pos[1],
            sizeX=self.size_hint[0],
            sizeY=self.size_hint[1],
            rgb=[
                self.background_color[0]*255,
                self.background_color[1]*255,
                self.background_color[2]*255,
                self.background_color[3],
            ],

        )
        noteToSave.save()

        logging.info('DB: Updated note with id: ' + str(self.noteId))


class ColoredLabelConfig(GridLayout):
    editing = Properties.BooleanProperty(False)
    noteid = Properties.NumericProperty()
    pinned = Properties.BooleanProperty()
    bcolor = Properties.ListProperty((0, 0, 0, 1))
    texto = Properties.StringProperty()

    def pinNote(self, noteId, pinned):
        ColoredLabel.visible = pinned != True
        self.pinned = pinned != True
        note = dbWrapper.findNoteById(noteId)
        note.pinned = pinned != True
        note.save()

    def on_editing(self, instance, value):
        if (value == False):
            nuevoTexto = self.ids.textValue.text
            noteToUpdate = Notes(_id=self.noteid, pinned=self.pinned, rgb=[
                                 self.bcolor[0]*255, self.bcolor[1]*255, self.bcolor[2]*255, 1], text=nuevoTexto)
            noteToUpdate.save()

    def deleteNote(self):
        dbWrapper.deleteNoteById(self.noteid)


class ButtonTextInput(TextInput, ButtonBehavior):
    pass


class DragLabel(DragBehavior, Label):
    pass


Builder.load_file("kv/dragImage.kv")


# TODO COULD BE DONE WITH SCATTER INSTEAD OF DRAG FOR SCALING AND ROTATION
# class DragImage(Scatter, AsyncImage):
class DragImage(DragBehavior, AsyncImage):
    saveOnDBEvent = Properties.ObjectProperty()
    imagenId = Properties.NumericProperty()

    def on_pos(self, instance, value):
        try:
            self.bringToFront()

            self.saveOnDBEvent.cancel()
        except:
            logging.info('Gifs: No previous event')

        self.saveOnDBEvent = Clock.schedule_once(self.saveOnDB, 5)

    def bringToFront(self):
        parent = self.parent
        children = parent.children
        childOnTop = children[0]

        if (self != childOnTop):
            parent.remove_widget(self)
            parent.add_widget(self)

    def saveOnDB(self, dt):
        # TODO SAVE SOURCE, POS AND SIZE ON DB

        gifToSave = Gifs(
            _id=self.imagenId,
            source=self.source,
            posX=self.pos[0],
            posY=self.pos[1],
            sizeX=self.size_hint[0],
            sizeY=self.size_hint[1],
            rotation=0,
            delay=self.anim_delay)
        gifToSave.save()

        logging.info('DB: Updated gif with id: ' + str(self.imagenId))


class GifConfig(ButtonBehavior, AsyncImage):
    imagenId = Properties.NumericProperty()
    pinned = Properties.BooleanProperty()
    delay = Properties.NumericProperty()

    def pinGif(self):

        self.pinned = not self.pinned

        gif = dbWrapper.findGifById(self.imagenId)
        gif.pinned = self.pinned
        gif.posX = 10
        gif.posY = 10
        gif.save()
