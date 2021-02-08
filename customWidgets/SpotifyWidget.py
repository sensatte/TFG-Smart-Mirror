from PIL import Image, ImageDraw
import numpy as np
import io
from kivy.core.image import Image as CoreImage
from kivy.core.window import Window
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from pyautogui import sleep
from utils.SpotifyWrapper import SpotifyWrapper
from utils.volume import CircularProgressBar
from kivy.clock import Clock
from kivy.animation import Animation
import kivy.properties as properties
import requests
from kivy.graphics import Color, Rectangle, Ellipse

from kivy.lang import Builder

import threading

import socket
# TODO QUE NO PETE SI NO HAY SPOTIFY RUNEANDO

# TODO que se actualice el volumen


kv_file = """
<SpotifyWidget>:
    size_hint:.5, .15

    GridLayout
        cols: 2
        rows:1

        Image:
            size_hint_x:None
            width:root.width/3
            id: songImage
            source: "images/menu/Spotify_bonico.png"
            canvas.before:
                PushMatrix
                Rotate:
                    angle: root.angle
                    axis: 0, 0, 1
                    origin: self.center
            canvas.after:
                PopMatrix

        BoxLayout
            orientation:"vertical"
            spacing:-self.height*.7
            Label:
                text: ""
                id: songName
                halign:'left'
                shorten: True
                font_size: root.width*0.05
                text_size: self.width, None
                size: self.texture_size

            Label:
                text: ""
                id: songArtist
                halign:'left'
                shorten: True
                font_size: root.width*0.05
                text_size: self.width, None
                size: self.texture_size

"""


Builder.load_string(kv_file)


class SpotifyWidget(RelativeLayout):
    angle=properties.NumericProperty()
    

    def __init__(self, **kwargs):
        super(SpotifyWidget, self).__init__(**kwargs)

        # Keyboard Handling for menuing
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.enabled = True
    
        self.spotifyWrapper = SpotifyWrapper(deviceName=socket.gethostname())

        self.deviceId = self.spotifyWrapper.getDeviceId()

        Clock.schedule_interval(self.update_label, 1)

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
                    self.spotifyWrapper.resume(deviceId=self.deviceId)
                    self.animSpin()
                else:
                    print("Pause")
                    self.spotifyWrapper.pause(deviceId=self.deviceId)
                    self.animSpinStop()
            elif keycode[1] == "d":
                print("Next")
                self.spotifyWrapper.next(deviceId=self.deviceId)
                pass
            elif keycode[1] == "a":
                print("Previous")
                self.spotifyWrapper.previous(deviceId=self.deviceId)
                pass
            elif keycode[1] == "w":
                print("VolUp")
                self.spotifyWrapper.volUp(deviceId=self.deviceId)
                self.volume=self.spotifyWrapper.getVolume()
                pass
            elif keycode[1] == "s":
                print("VolDown")
                self.spotifyWrapper.volDown(deviceId=self.deviceId)
                self.volume=self.spotifyWrapper.getVolume()
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
        song = self.spotifyWrapper.getCurrentSong()

        if (song != None):
            songName = song["name"]
            songArtist = song["album"]["artists"][0]["name"]
            songImage = song["album"]["images"][len(
                song["album"]["images"])-1]["url"]

            self.ids.songName.text = songName
            self.ids.songArtist.text = songArtist
            self.ids.songImage.texture = self.editSongImage(songImage)
            self.ids.songImage.texture.ask_update(None)
        else:
            songName = ""
            songImage = "images/menu/Spotify_bonico.png"
            self.ids.songName.text = songName
            self.ids.songName.source = songImage

    def editSongImage(self, songImage):

        response = requests.get(songImage)

        # Open the input image as numpy array, convert to RGB
        img = Image.open(io.BytesIO(response.content)).convert("RGB")
        npImage = np.array(img)
        h, w = img.size

        # Create same size alpha layer with circle
        alpha = Image.new('L', img.size, 0)
        draw = ImageDraw.Draw(alpha)
        draw.pieslice([0, 0, h, w], 0, 360, fill=255)

        # Convert alpha Image to numpy array
        npAlpha = np.array(alpha)

        # Add alpha layer to RGB
        npImage = np.dstack((npImage, npAlpha))

        imgIO = io.BytesIO()

        # Save with alpha
        Image.fromarray(npImage).save(imgIO, "png")

        imgIO.seek(0)
        imgData = io.BytesIO(imgIO.read())
        finalTexture = CoreImage(imgData, ext='png').texture

        return finalTexture

    
    def animSpin(self):
        anim = Animation(opacity=1, duration=.1)
        anim &= Animation(size_hint_y= 0.1, duration=.2)
        anim += Animation(size_hint_y= 0.15, duration=.2)
        anim.start(self)
        anim = Animation(angle = 360, duration=2) 
        anim += Animation(angle = 360, duration=2)
        anim.repeat = True
        anim.start(self)

    def animSpinStop(self):
        Animation.cancel_all(self, "angle")        
        anim = Animation(size_hint_y= 0.1, duration=.1)
        anim += Animation(size_hint_y= 0.15, duration=.2)
        anim += Animation(opacity=0, duration=.1)
        
        anim.start(self)

    def on_angle(self, item, angle):
        if angle == 360:
            item.angle = 0
