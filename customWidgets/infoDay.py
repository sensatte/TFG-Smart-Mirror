from customWidgets.infoDayResources.DateWidget import DateWidget
from customWidgets.infoDayResources.WeatherWidget import WeatherWidget
from customWidgets.infoDayResources.TempWidget import TempWidget
from customWidgets.infoDayResources.ClockWidget import ClockWidget
from kivy.uix.relativelayout import RelativeLayout
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

from kivy.lang import Builder
Builder.load_file('kv\\InfoDay.kv')

class InfoDay(RelativeLayout):
    def __init__(self, **kwargs):
        super(InfoDay, self).__init__(**kwargs)
        # self.size = Window.size
        # porcAncho=self.size_hint[0]
        # porcAlto=self.size_hint[1]
        # self.pos_hint={"x":0,"y":float(Window.height-(self.height*porcAlto))/Window.height}

        clock = ClockWidget()
        # self.add_widget(clock)

        date = DateWidget()
        # self.add_widget(date)

        temp = TempWidget()
        # self.add_widget(temp)

        weather = WeatherWidget()
        # self.add_widget(weather)

        tempwea=BoxLayout(orientation="horizontal")        
        tempwea.add_widget(temp)
        tempwea.add_widget(weather)

        print(self.height)
        datetemp=BoxLayout(orientation="horizontal", spacing=30, padding=[0,0,0,self.height/2])
        datetemp.add_widget(date)
        datetemp.add_widget(tempwea)

        res=BoxLayout(orientation="vertical")
        res.add_widget(clock)
        res.add_widget(datetemp)
        self.add_widget(res)


