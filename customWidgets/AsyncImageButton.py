from kivy.app import App
from kivy.uix.image import AsyncImage
from kivy.uix.behaviors import ButtonBehavior


class AsyncImageButton(ButtonBehavior, AsyncImage):
    pass
