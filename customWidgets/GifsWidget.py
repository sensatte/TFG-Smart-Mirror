from kivy.app import App
from kivy.uix.image import AsyncImage
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from customWidgets.utils.BehaviorUtil import DragImage
from kivy.properties import ListProperty
from db import dbWrapper

from kivy.lang import Builder
Builder.load_file("kv/gifsWidget.kv")


class GifsWidget(RelativeLayout):

    # TODO CREAR EL BUSCADOR DE GIFS

    images = ListProperty(dbWrapper.getAllGifs())

    def __init__(self, **kwargs):
        super(GifsWidget, self).__init__(**kwargs)

        for image in self.images:

            draggableImageWid = DragImage(
                imagenId=image._id,
                source=image.source,
                size_hint=(image.sizeX, image.sizeY),
                pos=(image.posX, image.posY),
                keep_ratio=False,
                allow_stretch=True,
                anim_delay=.05,
                mipmap=True,
            )

            self.add_widget(draggableImageWid)
