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
from kivy.uix.scatter import Scatter
from kivy.lang import Builder
from kivy.clock import Clock
import logging


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


class ColoredLabelConfig(ButtonBehavior, Label):
    noteid = Properties.NumericProperty()
    pinned = Properties.BooleanProperty()
    background_color = Properties.ListProperty((0, 0, 0, 1))

    def pinNote(self, noteId, pinned,):
        ColoredLabel.visible = pinned != True
        self.pinned = pinned != True
        note = dbWrapper.findNoteById(noteId)
        note.pinned = pinned != True

        note.save()


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
            self.saveOnDBEvent.cancel()
        except:
            logging.info('Gifs: No previous event')

        self.saveOnDBEvent = Clock.schedule_once(self.saveOnDB, 5)

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
