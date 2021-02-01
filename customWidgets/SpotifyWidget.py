from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from pyautogui import sleep
from utils.SpotifyWrapper import SpotifyWrapper

from kivy.graphics import Color, Rectangle

from kivy.lang import Builder

import threading

kv_file = """
<SpotifyWidget>:
    canvas.before:
        Color:
            rgba: (1, 1, 1, .2)
        Rectangle:
            pos: self.pos
            size: self.size
    Label:
        text: "Loading Song"
        id: songName
    Image:
        source: "images/menu/spotify.png"
        size_hint: (.3, .3)
"""

Builder.load_string(kv_file)


class SpotifyWidget(AnchorLayout):

    #TODO Ver alternatias al hilo del updateLabel

    def __init__(self, **kwargs):
        super(SpotifyWidget, self).__init__(**kwargs)

        self.size_hint = (0.3, 0.2)
        self.anchor_x = "left"
        self.anchor_y = "top"

        # Keyboard Handling for menuing
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.enabled = True

        self.spotifyWrapper = SpotifyWrapper()

        # self.spotifyIcon = Image(source="")
        # self.spotifyIcon.size_hint = (.3, .3)
        # self.spotifyIcon.pos_hint={"x":.1, "y":.9}
        # self.add_widget(self.spotifyIcon)

        test1 = self.ids["songName"]

        # self.test1 = Label(shorten=True,
        #                    shorten_from='right',
        #                    text_size=(200, 20))
        
        test1.canvas.add(Color(1., 1., 1, .2))
        test1.canvas.add(Rectangle(size=test1.size, post=test1.pos))

        #self.add_widget(test1)

        t = threading.Thread(target=self.updateLabel)
        t.setDaemon(True)
        t.start()

        #self.spotifyWrapper.play(self.spotifyWrapper.getMyPlaylists()[0]["uri"], self.spotifyWrapper.getDeviceId())

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
