from kivy.event import EventDispatcher
from kivy.uix.relativelayout import RelativeLayout
from utils.SpotifyWrapper2 import SpotifyWrapper2
from kivy.properties import StringProperty, ObjectProperty
import time
from threading import Thread
import logging

import socket

from kivy.lang import Builder
Builder.load_file('kv/spotify.kv')


class SpotifyWidget2(RelativeLayout, EventDispatcher):
    songName = StringProperty("Loading")
    wrapper = ObjectProperty(SpotifyWrapper2())
    deviceId = StringProperty(None)

    def __init__(self, **kwargs):
        super(SpotifyWidget2, self).__init__(**kwargs)

        t = Thread(target=threadGetDeviceId, args=(self,), daemon=True)
        t.start()

    def on_deviceId(self, instance, value):
        print("Got the deviceId ", value)
        # TODO AVISAR A TODO DE QUE TENEMOS ID Y POR LO TANTO TODO DEBERIA WORKEAR


def threadGetDeviceId(widget):
    foundDeviceId = None
    deviceName = socket.gethostname()

    while (widget.deviceId == None):
        logging.info('Spotipy: Looking for device ID')

        devicesList = widget.wrapper.getAllDevices()
        if (devicesList != None and len(devicesList) > 0):
            for device in devicesList:
                if (device["name"] == deviceName):
                    widget.deviceId = device["id"]
                    logging.info('Spotipy: Found device ID: '+widget.deviceId)
                    return

        time.sleep(1)
