from customWidgets.utils import oauth
import urllib.request
import json
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.clock import Clock

from kivy.lang import Builder
Builder.load_file('kv\\twitter.kv')

class TwitterWidget(GridLayout):
    
    def __init__(self, **kwargs):
        #TODO que puedas elegir si quieres RT, aunque entonces sería mejor aumentar los tweets que llegan
        super(TwitterWidget, self).__init__(**kwargs)
        self.chargeTweets("nada")
        Clock.schedule_interval(self.chargeTweets, 60)


    # Aquí introducimos nuestras claves de Twitter
    def oauth(self) :
        return { "consumer_key" : "Uonktan9L6quhLBMhiFqqxaoW",
            "consumer_secret" : "S48bu3HdqINVdvELnTIa6bUvVTpJcLbUf9bFy0nYg5kwzmLeXn",
            "token_key" : "727063220-qMIxtmN83jSBsgIAHUc43pRvPy61FxvcrdE2vUta",
            "token_secret" : "BAcGZQuOblv3jcETow4208B57EDGlcQYRw0wZ0n6rlMEJ" }

    # Esta función va a generar los parámetros necesarios para generar la URL
    def augment(self, url, parameters) :
        secrets = self.oauth()
        consumer = oauth.OAuthConsumer(secrets['consumer_key'], secrets['consumer_secret'])
        token = oauth.OAuthToken(secrets['token_key'],secrets['token_secret'])

        oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer, 
            token=token, http_method='GET', http_url=url, parameters=parameters)
        oauth_request.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(), consumer, token)
        return oauth_request.to_url()

    def chargeTweets(self,otro):
        self.clear_widgets()
        self.add_widget(Label(text= '[b]TWITTER TL[/b]', halign= 'left', font_size=10, markup=True))
        try:
            TWITTER_URL = 'https://api.twitter.com/1.1/statuses/home_timeline.json'

            n_tweets = 4

            url = self.augment(TWITTER_URL,
                        {'exclude_replies': 'false', 'count': n_tweets})

            connection = urllib.request.urlopen(url)

            data = connection.read().decode()
            js = json.loads(data)
            if len(js)>0:
                for k in range(0,len(js)):
                    tweet = js[k]['text']
                    author = js[k]['user']['name']
                    self.add_widget(LabelAjustado(text='[b]'+author+'[/b]' + ": " + tweet, colorb=k, max=len(js)-1))
            else:
                self.add_widget(LabelAjustado(text="No hay tweets que mostrar", colorb=0, max=0))
        except:
            self.add_widget(LabelAjustado(text="Se ha excedido el tiempo, prueba más tarde", colorb=0, max=0))

class LabelAjustado(Label):
    def __init__(self, text, colorb, max, **kwargs):
        super(LabelAjustado, self).__init__(**kwargs)
        self.text=text
        self.colorb = colorb
        self.max = max












