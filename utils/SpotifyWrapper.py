# Import libraries
import socket
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

    def __init__(self, deviceName):
        self.deviceName = deviceName
        self.scope = 'user-read-private user-read-playback-state user-modify-playback-state'
        self.spotifyObject = spotipy.Spotify(
            auth_manager=SpotifyOAuth(scope=self.scope))
        self.spotifyObject.requests_timeout = 20
        self.volume = 50
        self.paused = True

    def getSpotifyInstance(self):
        if (not self.spotifyObject):
            self.spotifyObject = spotipy.Spotify(
                auth_manager=SpotifyOAuth(scope=self.scope))
            self.spotifyObject.volume(self.volume, self.deviceId)
        return self.spotifyObject

    def getAllDevices(self):
        try:
            return self.getSpotifyInstance().devices()
        except IndexError as e:
            print("No devices found")
            return None

    def getDeviceId(self):
        try:
            devicesList = self.getSpotifyInstance().devices()['devices']
            print(devicesList)

            for device in devicesList:
                if (device["name"] == self.deviceName):
                    return device["id"]
            print("Current device not found. Are you running Spotify?")
            return None
        except IndexError as e:
            print("Current device not found. Are you running Spotify?")
            return None

    def getUser(self):
        return self.getSpotifyInstance().me()

    def getUserId(self):
        return self.getUser()["id"]

    def getUserPlaylists(self, userId, offset=0):
        return self.getSpotifyInstance().user_playlists(userId, offset=offset)

    def getSongsFromPlaylist(self, playlistId, userId):
        trackList = []
        playlist_tracks = self.getSpotifyInstance().user_playlist_tracks(
            user=userId, playlist_id=playlistId, fields='items')
        for data in playlist_tracks["items"]:
            track = data["track"]
            simplifiedTrack = {
                "artists": track["artists"],
                "duration_ms": track["duration_ms"],
                "id": track["id"],
                "name": track["name"],
                "uri": track["uri"]}
            trackList.append(simplifiedTrack)

        return trackList

    def getMyPlaylists(self, offset=0):
        return self.getUserPlaylists(self.getUserId(), offset=offset)["items"]

    def getCurrentPlaylist(self):
        return self.getSpotifyInstance().current_playback()

    def getCurrentSong(self):
        current_playing_track = self.getSpotifyInstance().current_user_playing_track()
        if (current_playing_track != None):
            return current_playing_track["item"]
        else:
            return None

    def play(self, uri, deviceId):
        self.getSpotifyInstance().start_playback(
            context_uri=uri, device_id=deviceId)

    def pause(self, deviceId):
        self.getSpotifyInstance().pause_playback(device_id=deviceId)
        self.paused = True

    def resume(self, deviceId):
        self.getSpotifyInstance().start_playback(device_id=deviceId)
        self.paused = False

    def next(self, deviceId):
        self.getSpotifyInstance().next_track(device_id=deviceId)

    def previous(self, deviceId):
        self.getSpotifyInstance().previous_track(device_id=deviceId)

    def volUp(self, deviceId):
        self.volume += 5
        if (self.volume > 100):
            self.volume = 100
        print(self.volume)
        self.getSpotifyInstance().volume(self.volume, device_id=deviceId)

    def volDown(self, deviceId):
        self.volume -= 5
        if (self.volume < 0):
            self.volume = 0
        print(self.volume)
        self.getSpotifyInstance().volume(self.volume, device_id=deviceId)


spotifyWrapper = SpotifyWrapper("DESKTOP-U5CE64C")
print(spotifyWrapper.getDeviceId())

print(spotifyWrapper.getCurrentSong())

#playlistId = spotifyWrapper.getMyPlaylists()[0]["id"]
#playlistUri = spotifyWrapper.getMyPlaylists()[0]["uri"]


#songs = spotifyWrapper.getSongsFromPlaylist(playlistId=playlistId, userId=spotifyWrapper.getUserId())

#spotifyWrapper.play(playlistUri, spotifyWrapper.getDeviceId())


#spotifyWrapper.play(uri=playlistUri, deviceId=spotifyWrapper.getDeviceId())

#print (spotifyWrapper.getCurrentSong())
