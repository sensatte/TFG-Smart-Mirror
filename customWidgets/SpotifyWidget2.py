from kivy.animation import Animation
from kivy.event import EventDispatcher
from kivy.uix.relativelayout import RelativeLayout
from utils.SpotifyWrapper2 import SpotifyWrapper2
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty, NumericProperty
import time
from threading import Thread
import logging
from kivy.loader import Loader

import socket

from kivy.lang import Builder
Builder.load_file('kv/spotify.kv')

# TODO PETA SOFT CUANDO SPOTIFY FUNCIONA PERO GETCURRENTSONG DA NULL POSYOQUESEPORQUE


class SpotifyWidget2(RelativeLayout, EventDispatcher):
    songName = StringProperty("Loading")
    songImageUrl = StringProperty("")
    wrapper = ObjectProperty(SpotifyWrapper2())
    deviceId = StringProperty(None)
    relaxing = BooleanProperty(True)
    songImageAngle = NumericProperty(0)
    paused = BooleanProperty(True)
    volume = NumericProperty(0)
    collapsed = BooleanProperty(False)
    playlistUri = StringProperty(
        "spotify:playlist:0lAKHIw0i0HZZMNqyIi29a")  # TODO GET FROM OPTIONS AND USAR

    def __init__(self, **kwargs):
        super(SpotifyWidget2, self).__init__(**kwargs)

        t = Thread(target=getDeviceIdThread, args=(self,), daemon=True)
        t.start()

    def on_volume(self, instance, value):
        if (self.deviceId != None):
            self.wrapper.setVolume(deviceId=self.deviceId, volume=value)

    def on_deviceId(self, instance, value):
        print("Got the deviceId ", value)
        self.relaxing = False

        self.volume = 50  # TODO GUARDAR EN MEMORIA EN VEZ DE HARDCODEAR
        t = Thread(target=getNewSongThread, args=(
            self,), daemon=True)
        t.start()
        # TODO AVISAR A TODO DE QUE TENEMOS ID Y POR LO TANTO TODO DEBERIA WORKEAR

    def relaxWithThePresses(self):
        t = Thread(target=relaxWithThePressesThread, args=(self,), daemon=True)
        t.start()

    def volUp(self):
        if (self.volume <= 95):
            self.volume += 5

    def volDown(self):
        if (self.volume >= 5):
            self.volume -= 5

    def on_paused(self, instance, value):
        if value:
            stopAnim(self)
        else:
            animSpin(self)


def animSpin(self):
    stopAnim(self)

    anim = Animation(songImageAngle=-360, duration=2)
    anim += Animation(songImageAngle=0, duration=0)
    anim.repeat = True
    anim.start(self)


def stopAnim(self):
    Animation.cancel_all(self)
    anim = Animation(songImageAngle=0, duration=0)
    anim.start(self)


def getNewSongThread(widget):
    while (True):
        logging.info('Spotipy: Looking for new song')
        song = widget.wrapper.getCurrentSong()
        if (song != None):
            try:
                if (song["name"] != widget.songName):
                    logging.info('Spotipy: Found new song: '+song["name"])
                    widget.songName = song["name"]
                    widget.songImageUrl = song["album"]["images"][-1]["url"].replace(
                        "https://", "")
                    # TODO IMAGEN DE LA CANCION
                    # return
            except:
                print("error")
                pass
        else:
            widget.wrapper.setPlaylist(
                deviceId=widget.deviceId, playlistUri=widget.playlistUri)
        time.sleep(1)


def getDeviceIdThread(widget):
    deviceName = socket.gethostname()

    while (widget.deviceId == None):
        logging.info('Spotipy: Looking for device ID')

        devicesList = widget.wrapper.getAllDevices()
        if (devicesList != None and len(devicesList) > 0):
            for device in devicesList:
                if (device["name"] == deviceName):
                    logging.info('Spotipy: Found device ID: '+device["id"])
                    widget.deviceId = device["id"]
                    return

        time.sleep(10)


def relaxWithThePressesThread(widget):
    logging.info('Spotipy: Stopped listening for a bit')
    widget.relaxing = True
    time.sleep(.5)
    widget.relaxing = False
    logging.info('Spotipy: Back to work!')
    return
