from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from ..utils.SpotifyWrapper import SpotifyWrapper

from datetime import datetime

class SpotifyWidget(AnchorLayout):
    
    def __init__(self, **kwargs):
        super(SpotifyWidget, self).__init__(**kwargs)

        #Keyboard Handling for menuing
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

        self.spotifyWrapper = SpotifyWrapper()

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'w':
            if (self.spotifyWrapper.getCurrentPlayBack() == 1):
                self.spotifyWrapper.playSong()
            else:
                self.spotifyWrapper.pauseSong()
        return True
        
        
        