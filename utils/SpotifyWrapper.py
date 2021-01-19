# Import libraries
import os
import sys
import json
import spotipy
import webbrowser
from spotipy.oauth2 import SpotifyOAuth
from json.decoder import JSONDecodeError

os.environ['SPOTIPY_CLIENT_ID'] = 'ca41eba604004e0c8d51cbcacfb4642b'
os.environ['SPOTIPY_CLIENT_SECRET'] = '71d4b96b520d41a5ab7d1fd5a1e2fcd5'
os.environ['SPOTIPY_REDIRECT_URI'] = 'https://works'

class SpotifyWrapper():

    def __init__ (self):
        self.scope = 'user-read-private user-read-playback-state user-modify-playback-state'
        self.spotifyObject = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=self.scope))

    def getSpotifyInstance(self):
        if (not self.spotifyObject):
            self.spotifyObject = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=self.scope))
        return self.spotifyObject

    def getDeviceId(self):
        return self.getSpotifyInstance().devices()['devices'][0]['id']

    def getUser(self):
        return self.getSpotifyInstance().me()

    def getUserId(self):
        return self.getUser()["id"]

    def getUserPlaylists(self, userId, offset=0):
        return self.getSpotifyInstance().user_playlists(userId, offset=offset)

    def getSongsFromPlaylist(self, playlist):
        #TODO
        trackList = playlist["items"][0]["asd"]

    def getMyPlaylists(self, offset=0):
        return self.getUserPlaylists(self.getUserId(), offset=offset)

    def playSong(self, songUri):
        trackSelectionList = []
        trackSelectionList.append(songUri)
        self.getSpotifyInstance().start_playback(self.getDeviceId(), songUri)


# spotifyWrapper = SpotifyWrapper()


# playlist_uri = spotifyWrapper.getMyPlaylists()["items"][0]["uri"]

# spotifyWrapper.playSong(playlist_uri)

