from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
import random

import requests
import json

id_endpoint = "https://type.fit/api/quotes"

from kivy.lang import Builder
Builder.load_file('kv\\quotes.kv')

import db.dbWrapper as dbWrapper

class QuotesWidget(AnchorLayout):
    
    def __init__(self, **kwargs):
        super(QuotesWidget, self).__init__(**kwargs)
        self.anchor_x = 'right'
        self.anchor_y = 'bottom'  

        quote = dbWrapper.getQuote()
        self.changeQuote(quote)
        

    def changeQuote(self, quoteList):
        self.ids["quoteid"].text=quoteList.text


# {'text': 'Genius is one percent inspiration and ninety-nine percent perspiration.', 'author': 'Thomas Edison'}






