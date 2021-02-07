from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from pyautogui import sleep
from utils.SpotifyWrapper import SpotifyWrapper
from kivy.clock import Clock

from kivy.graphics import Color, Rectangle

from kivy.lang import Builder

import threading

import socket
# TODO QUE NO PETE SI NO HAY SPOTIFY RUNEANDO

# TODO BONITO

# TODO QUE SE VEA EL VOLUMEN, MAYBE UNA IMAGEN POR TRES NIVELES


kv_file = """
<SpotifyWidget>:

    canvas:
        Color:
            rgba: 0.2,0.5,0.4,1
        Rectangle:
            pos: 0,0
            size: self.size

    Label:
        text: "No song found"
        id: songName

    Image:
        source: "images/menu/spotify.png"
        pos_hint: {"center_x":.3, "center_y":.7}
        size_hint: (.3, .3)
"""

Builder.load_string(kv_file)


class SpotifyWidget(RelativeLayout):

    def __init__(self, **kwargs):
        super(SpotifyWidget, self).__init__(**kwargs)

        # Keyboard Handling for menuing
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.enabled = True

        self.spotifyWrapper = SpotifyWrapper(deviceName=socket.gethostname())

        self.deviceId = self.spotifyWrapper.getDeviceId

        songName = self.ids["songName"]

        Clock.schedule_interval(self.update_label, .5)

        # t = threading.Thread(target=self.updateLabel)
        # t.setDaemon(True)
        # t.start()

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):

        if (self._keyboard.enabled):

            if keycode[1] == 'enter':
                if (self.spotifyWrapper.getCurrentPlaylist() == None or self.spotifyWrapper.getCurrentPlaylist()["is_playing"] == False):
                    print("Resume")
                    self.spotifyWrapper.resume()
                else:
                    print("Pause")
                    self.spotifyWrapper.pause()
            elif keycode[1] == "d":
                print("Next")
                self.spotifyWrapper.next()
                pass
            elif keycode[1] == "a":
                print("Previous")
                self.spotifyWrapper.previous()
                pass
            elif keycode[1] == "w":
                print("VolUp")
                self.spotifyWrapper.volUp()
                pass
            elif keycode[1] == "s":
                print("VolDown")
                self.spotifyWrapper.volDown()
                pass

        return True

    def disableKeyboardIndefinitely(self):
        self._keyboard.enabled = False

    def enableKeyboard(self):
        self._keyboard.enabled = True

    def disableKeyboard(self):
        #print("Disabled keyboard")
        self._keyboard.enabled = False
        sleep(1)
        self._keyboard.enabled = True
        #print("Enabled keyboard")
        exit()

    def update_label(self, *args):
        songName = self.spotifyWrapper.getCurrentSong()
        # print(songName)
        self.ids.songName.text = songName

    # def updateLabel(self):
    #     previousSongName = None
    #     test1 = self.ids["songName"]
    #     if(previousSongName == None or self.spotifyWrapper.getCurrentSong()["name"] != previousSongName):
    #         test1.text = self.spotifyWrapper.getCurrentSong()["name"]
    #         previousSongName = test1.text
