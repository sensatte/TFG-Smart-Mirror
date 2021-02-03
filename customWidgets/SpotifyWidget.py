from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from pyautogui import sleep
from utils.SpotifyWrapper import SpotifyWrapper

from kivy.graphics import Color, Rectangle

from kivy.lang import Builder

import threading


kv_file = """
<SpotifyWidget>:

    canvas:
        Color:
            rgba: 0.2,0.5,0.4,1
        Rectangle:
            pos: 0,0
            size: self.size

    Label:
        text: "Loading Song"
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

        self.spotifyWrapper = SpotifyWrapper()

        test1 = self.ids["songName"]

        t = threading.Thread(target=self.updateLabel)
        t.setDaemon(True)
        t.start()

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):

        if (self._keyboard.enabled):

            if keycode[1] == 'enter':
                if (self.spotifyWrapper.getCurrentPlaylist()["is_playing"] == False):
                    # print("Resume")
                    self.spotifyWrapper.resume(
                        deviceId=self.spotifyWrapper.getDeviceId())
                else:
                    # print("Pause")
                    self.spotifyWrapper.pause(
                        deviceId=self.spotifyWrapper.getDeviceId())
            elif keycode[1] == "d":
                # print("Next")
                self.spotifyWrapper.next(
                    deviceId=self.spotifyWrapper.getDeviceId())
                pass
            elif keycode[1] == "a":
                # print("Previous")
                self.spotifyWrapper.previous(
                    deviceId=self.spotifyWrapper.getDeviceId())
                pass
            # print("Current song")
            # print(self.spotifyWrapper.getCurrentSong()["name"])

            keyboardInterrupter = threading.Thread(target=self.disableKeyboard)
            keyboardInterrupter.setDaemon(True)
            keyboardInterrupter.start()

        return True

    def disableKeyboard(self):
        #print("Disabled keyboard")
        self._keyboard.enabled = False
        sleep(1)
        self._keyboard.enabled = True
        #print("Enabled keyboard")
        exit()

    def updateLabel(self):
        previousSongName = None
        test1 = self.ids["songName"]
        while(True):
            # print("loop")
            if (previousSongName == None or self.spotifyWrapper.getCurrentSong()["name"] != previousSongName):
                test1.text = self.spotifyWrapper.getCurrentSong()["name"]
                previousSongName = test1.text
            sleep(0.5)
