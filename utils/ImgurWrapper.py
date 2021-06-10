from imgurpython import ImgurClient
from imgurpython.helpers import GalleryAlbum
import os
import urllib.parse

os.environ['IMGUR_CLIENT_ID'] = '2fe13e5fb7324d1'
os.environ['IMGUR_CLIENT_SECRET'] = '5497654450389d556ef0de11c4f1b1a022ca11c3'


class ImgurWrapper():

    imgurObject = ImgurClient(
        client_id=os.environ['IMGUR_CLIENT_ID'], client_secret=os.environ['IMGUR_CLIENT_SECRET'])

    albumId = "aceituna"

    def getImage(self, imageId):
        return self.imgurObject.get_image(image_id=imageId)

    def search(self, query):
        response = self.imgurObject.gallery_search(
            q=query,
            sort="time",
        )

        linksList = []

        for item in response:
            if isinstance(item, GalleryAlbum):
                for item2 in item.images:
                    linksList.append(item2["link"])
            else:
                linksList.append(item.link)

        return linksList
