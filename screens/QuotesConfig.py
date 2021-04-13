# pylint: disable=no-member

from kivy.uix.screenmanager import ScreenManager, Screen
import kivy.properties as Properties
from kivy.app import App
from functools import partial
from kivy.uix.screenmanager import FadeTransition
from kivy.animation import Animation
import random

import requests
import json

id_endpoint = "https://type.fit/api/quotes"

#import kv
from kivy.lang import Builder
Builder.load_file('kv\\quotesConfig.kv')

import db.dbWrapper as dbWrapper

class QuotesConfig(Screen):
    #TODO tema de longituf

    quoteList= Properties.ListProperty()
    colorInter=Properties.ListProperty([1,1,1,1])
    currentQuote = Properties.StringProperty('Genius is one percent inspiration and ninety-nine percent perspiration.' + "\n- " + 'Thomas Edison')
    currentFont = Properties.StringProperty('MelanieRoselyn')
    activeInter=Properties.BooleanProperty(False)

    def __init__(self, **kwargs):
        super(QuotesConfig, self).__init__(**kwargs)
        self.pos_hint={'center_y': 0.5, 'center_x': 0.5}           

        #Cambio a fuente
        self.changeFont('MelanieRoselyn')

        #Recojo todas las quotes
        self.quoteList = self.getQuotes()



    def changeFont(self, font):
        # fonts=['Baby Darling', 'Berkah Ramadhan', 'MelanieRoselyn', 'Pumpkin Story', 'Good Mood',
        #     'Revans-Medium', 'Silent Landfield', 'Winter Creative', 'Hallington']
        self.ids["quoteid"].font_name='fonts\\' + font
        self.currentFont = font


    #Recoge todas las frases
    def getQuotes(self):
        res = {}

        request = requests.get(id_endpoint)

        if request.status_code != 200:
            pass

        else:
            res = json.loads(request.text)

        return res

    def changeQuote(self): 
        quoteList=self.quoteList    
        quote={"quote","author"}
        ran = random.randint(0, len(quoteList))

        if ((quoteList[ran]["text"] != None) and (quoteList[ran]["author"] != None)):
            quote = quoteList[ran]

        elif ((quoteList[ran]["text"] != None) and (quoteList[ran]["author"] == None)):
            quote = {'text': quoteList[ran]["text"], 'author': 'Anonimous'}

        else: quote={'text': "Error!", 'author': 'Error!'}
        
        self.ids["quoteid"].text=quote["text"] + "\n- " + quote["author"]
        self.currentQuote = quote["text"] + "\n- " + quote["author"]


    def saveConfig(self):
        #guardar las configs
        print(self.activeInter)
        dbWrapper.saveQuote(self.activeInter, self.currentQuote, self.currentFont, self.colorInter)        

    def pressedBack(self, widget):
        anim = Animation(pos_hint={"center_x": .5, "y": -.03}, duration=.1)
        anim += Animation(pos_hint={"center_x": .5, "y": 0}, duration=.1)
        anim.bind(on_complete=partial(self.goToMenuScreen))
        anim.start(widget)

    def goToMenuScreen(self, widget, selected):        
        self.saveConfig()
        App.get_running_app().root.transition = FadeTransition(duration=.3)
        App.get_running_app().root.current = "menu"