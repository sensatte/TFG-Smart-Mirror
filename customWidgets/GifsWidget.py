from kivy.app import App
from kivy.uix.image import AsyncImage
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from customWidgets.utils.BehaviorUtil import DragImage, ScatterImage
from kivy.properties import ListProperty
from db import dbWrapper

from kivy.lang import Builder
Builder.load_file("kv/gifsWidget.kv")


class GifsWidget(FloatLayout):

    # TODO CREAR EL BUSCADOR DE GIFS

    def __init__(self, **kwargs):
        super(GifsWidget, self).__init__(**kwargs)
        self.__name__ = "gifs"

        self.images = dbWrapper.getPinnedGifs()

        for image in self.images:

            # imageWid = DragImage(
            #     imagenId=image._id,
            #     source=image.source,
            #     size_hint=(image.sizeX, image.sizeY),
            #     pos=(image.posX, image.posY),
            #     keep_ratio=False,
            #     allow_stretch=True,
            #     anim_delay=image.delay,
            #     mipmap=True,
            # )

            imageWid = ScatterImage(
                imagenId=image._id,
                source=image.source,
                # size_hint=(image.sizeX, image.sizeY),
                scale=image.scale,
                rotation=image.rotation,
                pos=(image.posX, image.posY),
                anim_delay=image.delay,
            )

            self.add_widget(imageWid)
