from kivy.uix.scatterlayout import ScatterLayout
from customWidgets.infoDayResources.DateWidget import DateWidget
from customWidgets.infoDayResources.WeatherWidget import WeatherWidget
from customWidgets.infoDayResources.TempWidget import TempWidget
from customWidgets.infoDayResources.ClockWidget import ClockWidget
from customWidgets.infoDayResources.InternationalWidget import InternationalWidget
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from customWidgets.utils.BehaviorUtil import DraggableBaseWidget
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

from kivy.lang import Builder

Builder.load_file('kv/infoDay.kv')


class InfoDayWidget(DraggableBaseWidget):
    def __init__(self, **kwargs):
        super(InfoDayWidget, self).__init__(**kwargs)
        self.__name__ = "info"
        self.dbName = "infoDay"
        self.size_hint = (.3, .15)
        clock = ClockWidget(size_hint=(1, .7))
        date = DateWidget()
        temp = TempWidget()
        weather = WeatherWidget()
        info = InternationalWidget()

        tempwea = BoxLayout(orientation="horizontal")
        tempwea.add_widget(temp)
        tempwea.add_widget(weather)

        datetemp = BoxLayout(orientation="horizontal",
                             spacing=30,
                             padding=[10, 0, 0, 0],
                             size_hint=(1, 0.25))
        datetemp.add_widget(date)
        datetemp.add_widget(tempwea)

        res = BoxLayout(orientation="vertical",
                        size_hint=(1, .8),
                        padding=[10, 10, 0, 0],
                        spacing=-self.width / 20)
        res.add_widget(clock)
        res.add_widget(datetemp)
        res.add_widget(info)

        self.add_widget(res)
