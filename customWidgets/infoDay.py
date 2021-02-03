from customWidgets.infoDayResources.DateWidget import DateWidget
from customWidgets.infoDayResources.WeatherWidget import WeatherWidget
from customWidgets.infoDayResources.TempWidget import TempWidget
from customWidgets.infoDayResources.ClockWidget import ClockWidget
from kivy.uix.relativelayout import RelativeLayout
from kivy.core.window import Window
from kivy.uix.relativelayout import RelativeLayout

from kivy.lang import Builder
Builder.load_file('kv\\dayInfo.kv')

class InfoDay(RelativeLayout):
    def __init__(self, **kwargs):
        super(InfoDay, self).__init__(**kwargs)
        self.size = Window.size
        porcAncho=self.size_hint[0]
        porcAlto=self.size_hint[1]
        self.pos_hint={"x":0,"y":float(Window.height-(self.height*porcAlto))/Window.height}

        # ancho=self.pos_hint["x"]
        # alto=self.pos_hint["y"]
        
        clock = ClockWidget()
        # clock.pos_hint = {"x": (self.width*porcAncho)/Window.width,"y": alto-0.1}
        # clock.text_size=[20,51]
        # print(self.width,self.size, self.pos_hint, clock.pos_hint, clock.size)
        self.add_widget(clock)
        
        date = DateWidget()
        self.add_widget(date)

        temp = TempWidget()
        self.add_widget(temp)

        weather = WeatherWidget()
        self.add_widget(weather)


