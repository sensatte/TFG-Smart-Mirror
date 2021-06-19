from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
import customWidgets.utils.BehaviorUtil as BehaviorUtil
import db.dbWrapper as dbWrapper
from kivy.app import App
from kivy.lang import Builder
Builder.load_file('kv/notes.kv')


class NotesWidget(FloatLayout):
    # TODO textos laargos comprimir

    def __init__(self, **kwargs):
        super(NotesWidget, self).__init__(**kwargs)
        self.__name__ = "notas"

        showNotes(self)


def showNotes(self):
    noteList = dbWrapper.getAllNotes()
    num = 0
    for note in noteList:
        if(num < 9 and note.pinned == True):
            num += 1

            label = BehaviorUtil.ScatterColoredLabel(
                noteId=note._id,
                visible=note.pinned,
                text=note.text,
                background_color=(
                    note.rgb[0]/255, note.rgb[1]/255, note.rgb[2]/255, note.rgb[3]),
                scale=note.scale,
                rotation=note.rotation,
            )
            label.pos = (note.posX, note.posY)
            self.add_widget(label)


def deleteNotes(self):
    self.remove_widget(self.children)
    self.showNotes()
