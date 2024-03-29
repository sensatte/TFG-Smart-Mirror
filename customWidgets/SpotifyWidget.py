from kivy.animation import Animation
from kivy.event import EventDispatcher
from kivy.uix.relativelayout import RelativeLayout
from utils.SpotifyWrapper import SpotifyWrapper
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty, NumericProperty
import time
from threading import Thread
import logging
from kivy.loader import Loader
from customWidgets.AsyncImageButton import AsyncImageButton

from kivy.lang import Builder
Builder.load_file('kv/spotify.kv')

# TODO PETA SOFT CUANDO SPOTIFY FUNCIONA PERO GETCURRENTSONG DA NULL POSYOQUESEPORQUE


class SpotifyWidget(RelativeLayout, EventDispatcher):
    songName = StringProperty("Loading")
    songImageUrl = StringProperty("")
    wrapper = ObjectProperty(SpotifyWrapper())
    deviceId = StringProperty(None)
    relaxing = BooleanProperty(True)
    songImageAngle = NumericProperty(0)
    paused = BooleanProperty(False)
    volume = NumericProperty(0)
    collapsed = BooleanProperty(True)
    playListURI = StringProperty("")
    shuffle = StringProperty("")

    def pauseResume(self):
        try:
            self.wrapper.pauseResume(self.deviceId)
        except:
            #PETA PORQUE NO ESTA EL DEVICE, ASI QUE RECARGAMOS EL WIDGET
            self.parent.reloadSpotify()

    def next(self):
        try:
            self.wrapper.next(self.deviceId)
        except:
            #PETA PORQUE NO ESTA EL DEVICE, ASI QUE RECARGAMOS EL WIDGET
            self.parent.reloadSpotify()

    def previous(self):
        try:
            self.wrapper.previous(self.deviceId)
        except:
            #PETA PORQUE NO ESTA EL DEVICE, ASI QUE RECARGAMOS EL WIDGET
            self.parent.reloadSpotify()

    def __init__(self, **kwargs):
        super(SpotifyWidget, self).__init__(**kwargs)

        t = Thread(target=getDeviceIdThread, args=(self,), daemon=True)
        t.start()

    def on_volume(self, instance, value):
        if (self.deviceId != None):
            try:
                self.wrapper.setVolume(deviceId=self.deviceId, volume=value)
            except:
                #PETA PORQUE NO ESTA EL DEVICE, ASI QUE RECARGAMOS EL WIDGET
                self.parent.reloadSpotify()

    def on_playListURI(self, instance, value):
        self.wrapper.setPlaylist(
            playlistUri=value, deviceId=self.deviceId)
        animSpin(self)

    def on_shuffle(self, instance, value):
        #self.wrapper.shuffle(deviceId=self.deviceId, value=value)
        pass

    def on_deviceId(self, instance, value):
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

    def on_collapsed(self, instance, value):
        pauseButton = self.ids.startPauseButton
        nextButton = self.ids.nextButton
        previousButton = self.ids.previousButton
        songImage = self.ids.songImage
        volUp = self.ids.volUp
        volDown = self.ids.volDown

        all = [pauseButton, nextButton,
               previousButton, volUp, volDown]

        inTransition = "in_back"
        outTransition = "out_bounce"

        if (value):
            # COLLAPSED
            volUp.pos = (100, 100)

            imageAnim = songImageAnim = Animation(
                size_hint=(.7, .7), transition=inTransition, duration=.6)

            anim = Animation(
                pos_hint={'center_x': 0.5, "center_y": .5}, duration=.5, transition=inTransition) & Animation(opacity=0, duration=1)

            for widget in all:
                anim.start(widget)

            imageAnim.start(songImage)

        else:
            # UNCOLLAPSED
            songImageAnim = Animation(
                size_hint=(.5, .5), transition=outTransition)

            pauseAnim = Animation(
                pos_hint={"center_x": .5, "center_y": .1}, duration=1, transition=outTransition) & Animation(opacity=1, duration=1)

            nextAnim = Animation(
                pos_hint={"center_x": .75, "center_y": .2}, duration=1, transition=outTransition) & Animation(opacity=1, duration=1)
            previousAnim = Animation(
                pos_hint={"center_x": .25, "center_y": .2}, duration=1, transition=outTransition) & Animation(opacity=1, duration=1)
            volUpAnim = Animation(
                pos_hint={"center_x": .66, "center_y": .85}, duration=1, transition=outTransition) & Animation(opacity=1, duration=1)
            volDownAnim = Animation(
                pos_hint={"center_x": .33, "center_y": .85}, duration=1, transition=outTransition) & Animation(opacity=1, duration=1)

            songImageAnim.start(songImage)

            pauseAnim.start(pauseButton)
            nextAnim.start(nextButton)
            previousAnim.start(previousButton)
            volUpAnim.start(volUp)
            volDownAnim.start(volDown)

    def pushedButtonAnim(self, widget):
        inTransition = "in_back"
        outTransition = "out_bounce"
        anim = Animation(size_hint=(.15, .2), duration=.2,
                         transition=inTransition)
        anim += Animation(size_hint=(.2, .25), duration=.3,
                          transition=outTransition)
        anim.start(widget)


def animSpin(self):
    stopAnim(self)

    anim = Animation(songImageAngle=-360, duration=3.5)
    anim += Animation(songImageAngle=0, duration=0)
    anim.repeat = True
    anim.start(self)


def stopAnim(self):
    Animation.cancel_all(self)
    anim = Animation(songImageAngle=0, duration=0)
    anim.start(self)


def getNewSongThread(widget):
    while (True):
        f = open("spotifyPlaylistURI.txt", "r")
        currentPlaylistURI = f.read()
        f.close()
        widget.playListURI = currentPlaylistURI
        try:
            f = open("spotifyShuffle.txt", "r")
            shuffle = f.read()
            f.close()
        except:
            shuffle = False
        widget.shuffle = shuffle
        logging.info('Spotipy: Looking for new song')
        song = widget.wrapper.getCurrentSong()
        if (song != None):
            try:
                if (song["item"]["name"] != widget.songName):
                    logging.info('Spotipy: Found new song: ' +
                                 song["item"]["name"])
                    widget.songName = song["item"]["name"]
                    widget.songImageUrl = song["item"]["album"]["images"][-1]["url"].replace(
                        "https://", "")

            except:
                print("error")
                print(song)
                pass
        else:
            pass
        time.sleep(2.5)

def getDeviceIdThread(widget):
    deviceName = "Web Player (Chrome)"

    time.sleep(60)

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
