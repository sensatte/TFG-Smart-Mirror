from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
import random

import requests
import json

id_endpoint = "https://type.fit/api/quotes"

from kivy.lang import Builder
Builder.load_file('kv\\quotes.kv')

class QuotesWidget(AnchorLayout):
    
    def __init__(self, **kwargs):
        super(QuotesWidget, self).__init__(**kwargs)
        self.anchor_x = 'right'
        self.anchor_y = 'bottom'        
        
        #TODO hay frases muy largas, debería ajustarse según tamaño
        #TODO tb hay frases con números que parecen no imprimir bien los carqacteres?)

        #de momento está puesto que sea random, hasta que no se haga config nada
        #Cambio a fuente aleatoria
        ran=random.randint(0, len(fonts)-1)
        changeFont(self, ran)

        #Recojo todas las quotes
        quoteList = getQuotes(self)

        #Cambio el texto de la label
        changeQuote(self, quoteList)

fonts=['Baby Darling', 'Berkah Ramadhan', 'MelanieRoselyn', 'Pumpkin Story', 'Good Mood',
            'Revans-Medium', 'Silent Landfield', 'Winter Creative', 'Hallington']

def changeFont(self, font):
    # print(fonts[font])
    self.ids["quoteid"].font_name='fonts\\' + fonts[font]


#Recoge todas las frases
def getQuotes(self):
    res = {}

    request = requests.get(id_endpoint)

    if request.status_code != 200:
        pass

    else:
        res = json.loads(request.text)

    return res

def changeQuote(self, quoteList):     
    quote={"quote","author"}
    ran = random.randint(0, len(quoteList))

    if ((quoteList[ran]["text"] != None) and (quoteList[ran]["author"] != None)):
        quote = quoteList[ran]

    elif ((quoteList[ran]["text"] != None) and (quoteList[ran]["author"] == None)):
        quote = {'text': quoteList[ran]["text"], 'author': 'Anonimous'}

    else: quote={'text': "Error!", 'author': 'Error!'}
    
    self.ids["quoteid"].text=quote["text"] + "\n- " + quote["author"]


# {'text': 'Genius is one percent inspiration and ninety-nine percent perspiration.', 'author': 'Thomas Edison'}






