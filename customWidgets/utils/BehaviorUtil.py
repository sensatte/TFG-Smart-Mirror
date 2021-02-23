from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.app import App
import kivy.properties as Properties


class ImageButton(ButtonBehavior, Image):
    pass

class Scrolling(ScrollView):
    pass

class ColoredLabel(Label):
    background_color = Properties.ListProperty((0,0,0,1))

class ColoredLabelConfig(ButtonBehavior, Label):
    pinned = Properties.BooleanProperty()
    background_color = Properties.ListProperty((0,0,0,1))

    # def pinNote(self, state): 
    #     print(App.get_running_app.noteList)
        # data["location"] = "NewPath"

        # with open("db/notes.json", "w") as jsonFile:
        #     json.dump(data, jsonFile)


