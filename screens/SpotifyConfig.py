# pylint: disable=no-member

import os
from kivy.uix.screenmanager import ScreenManager, Screen
import kivy.properties as Properties
from kivy.uix.image import Image
from kivy.app import App
from kivy.animation import Animation
from functools import partial
from kivy.uix.screenmanager import FadeTransition
from kivy.uix.togglebutton import ToggleButton
from customWidgets.utils.BehaviorUtil import ImageButton, Scrolling
from kivy.properties import ObjectProperty
from utils.SpotifyWrapper2 import SpotifyWrapper2
from customWidgets.utils.BehaviorUtil import PlayListToggle
from functools import partial

#import kv
from kivy.lang import Builder
Builder.load_file('kv/spotifyConfig.kv')
import db.dbWrapper as dbWrapper

class SpotifyConfig(Screen):

    wrapper = ObjectProperty(SpotifyWrapper2())
    activeInter = Properties.BooleanProperty(True)

    def __init__(self, **kwargs):
        super(SpotifyConfig, self).__init__(**kwargs)
        self.pos_hint = {'center_y': 0.5, 'center_x': 0.5}

        playlistsLayout = self.ids.playlistsLayout

        shuffleOn = self.ids.shuffleOn
        shuffleOff = self.ids.shuffleOff
        f = open("spotifyShuffle.txt", "r")
        currentShuffle = f.read()
        f.close()
        if (currentShuffle == "true"):
            shuffleOn.state = "down"
        else:
            shuffleOff.state = "down"

        # TODO QUE SE COJAN TODAS LAS PLAYLISTS Y NO SOLO LAS QUE EL USER CREÓ
        allPlaylists = self.wrapper.getPlaylists()

        f = open("spotifyPlaylistURI.txt", "r")
        currentPlaylistURI = f.read()
        f.close()

        for playlist in allPlaylists:
            songToggleButton = PlayListToggle()
            songToggleButton.text = playlist["name"]
            songToggleButton.source = playlist["images"][0]["url"]
            songToggleButton.on_press = partial(
                self.chosenPlaylist, playlist["uri"])
            if playlist["uri"] == currentPlaylistURI:
                songToggleButton.state = "down"
            playlistsLayout.add_widget(songToggleButton)

    def chosenPlaylist(self, playlistURI):
        print(playlistURI)
        f = open("spotifyPlaylistURI.txt", "w")
        f.write(playlistURI)
        f.close()

    def chosenShuffle(self, option):
        print(option)
        f = open("spotifyShuffle.txt", "w")
        f.write(option)
        f.close()

    def saveConfig(self):
        #guardar las configs
        print(self.activeInter)
        dbWrapper.saveSpotify(self.activeInter)

    def pressedBack(self, widget):
        anim = Animation(pos_hint={"center_x": .5, "y": -.03}, duration=.1)
        anim += Animation(pos_hint={"center_x": .5, "y": 0}, duration=.1)
        anim.bind(on_complete=partial(self.goToMenuScreen))
        anim.start(widget)

    def goToMenuScreen(self, widget, selected):
        self.saveConfig()
        App.get_running_app().root.transition = FadeTransition(duration=.3)
        App.get_running_app().root.current = "menu"
