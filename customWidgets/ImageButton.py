from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

# from kivy.lang import Builder
# Builder.load_file("kv/imageButton.kv")


class ImageButton(ButtonBehavior, Image):
    # def __init__(self, onPress, onRelease, **kwargs):
    #     super(ImageButton, self).__init__(**kwargs)
    #     if (onPress != None):
    #         self.on_press = onPress
    #     if (onRelease != None):
    #         self.on_release = onRelease
    pass
