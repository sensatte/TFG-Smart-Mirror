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

        self.relaxing = False

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

    def getCurrentPlaylist(self):
        return self.getSpotipyInstance().current_playback()

    def getCurrentSong(self):
        return self.getSpotipyInstance().current_user_playing_track()["item"]

    def pause(self, deviceId):
        self.getSpotipyInstance().pause_playback(device_id=deviceId)

    def resume(self, deviceId):
        self.getSpotipyInstance().start_playback(device_id=deviceId)

    def pauseResume(self, deviceId):
        if deviceId != None:
            currentPlaylist = self.getCurrentPlaylist()
            if (currentPlaylist == None or currentPlaylist["is_playing"] == False):
                print("Resume")
                self.resume(deviceId=deviceId)
            else:
                print("Pause")
                self.pause(deviceId=deviceId)

    def next(self, deviceId):
        self.getSpotipyInstance().next_track(device_id=deviceId)

    def previous(self, deviceId):
        self.getSpotipyInstance().previous_track(device_id=deviceId)

    def setVolume(self, deviceId, volume):
        self.getSpotipyInstance().volume(volume_percent=volume, device_id=deviceId)

# wrapper = SpotifyWrapper2()

# print(wrapper.getCurrentSong())
