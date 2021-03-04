from kivy.uix.behaviors.togglebutton import ToggleButtonBehavior
from kivy.uix.image import AsyncImage, Image
from kivy.uix.behaviors import ButtonBehavior, DragBehavior
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.app import App
import kivy.properties as Properties
import db.dbWrapper as dbWrapper
from kivy.uix.scatter import Scatter
from kivy.lang import Builder
from kivy.clock import Clock
import logging


class ImageButton(ButtonBehavior, Image):
    pass


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
class DragImage(DragBehavior, AsyncImage):
    saveOnDBEvent = Properties.ObjectProperty()
    imagenId = Properties.NumericProperty()

    def on_pos(self, instance, value):
        try:
            self.saveOnDBEvent.cancel()
        except:
            logging.info('Gifs: No previous event')

        self.saveOnDBEvent = Clock.schedule_once(self.saveOnDB, 5)

    pass

    def saveOnDB(self, dt):
        # TODO SAVE SOURCE, POS AND SIZE ON DB
        dbWrapper.updateGif(
            _id=self.imagenId,
            source=self.source,
            pos=self.pos,
            size_hint=self.size_hint,
            rotation=0)
