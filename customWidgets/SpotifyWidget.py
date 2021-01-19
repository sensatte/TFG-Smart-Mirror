from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from ..utils.SpotifyWrapper import SpotifyWrapper

from datetime import datetime

class SpotifyWidget(AnchorLayout):
    
    def __init__(self, **kwargs):
        super(SpotifyWidget, self).__init__(**kwargs)
        
        self.spotifyWrapper = SpotifyWrapper()
        
        