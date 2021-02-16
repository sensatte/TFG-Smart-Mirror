# TODO WRAPPER 2

import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth


os.environ['SPOTIPY_CLIENT_ID'] = 'ca41eba604004e0c8d51cbcacfb4642b'
os.environ['SPOTIPY_CLIENT_SECRET'] = '71d4b96b520d41a5ab7d1fd5a1e2fcd5'
os.environ['SPOTIPY_REDIRECT_URI'] = 'https://works'


class SpotifyWrapper2():

    def __init__(self):
        self.scope = 'user-read-private user-read-playback-state user-modify-playback-state'
        self.spotifyObject = spotipy.Spotify(
            auth_manager=SpotifyOAuth(scope=self.scope))
        self.spotifyObject.requests_timeout = 20

    def getSpotipyInstance(self):
        if (not self.spotifyObject):
            self.spotifyObject = spotipy.Spotify(
                auth_manager=SpotifyOAuth(scope=self.scope))
            self.spotifyObject.volume(self.volume, self.deviceId)
        return self.spotifyObject

    def getAllDevices(self):
        try:
            return self.getSpotipyInstance().devices()['devices']
        except IndexError as e:
            print("No devices found")
            return None

    def loadNextSong(self, deviceId):
        # TODO
        pass
