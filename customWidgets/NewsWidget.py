from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class NewsWidget(BoxLayout):
    
    def __init__(self, **kwargs):
        super(NewsWidget, self).__init__(**kwargs)
        self.anchor_x = 'center'
        self.anchor_y = 'center'
        self.orientation='vertical'
        self.size_hint =(.2, .2)
        self.pos_hint ={"x":0.7, "y":0.7}
                
        news = ["Noticia falsa 1",
                "Trump decide crear DOS muros",
                "Al corona le entró corona: la autodestrucción",
                "No se que mas inventarme jo"]
            
        for new in news:
            self.add_widget(Label(text=new,
                                  shorten=True,
                                  shorten_from='right',
                                  text_size=(200,20)
                                  ))

