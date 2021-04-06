from kivy.uix.scatterlayout import ScatterLayout
from customWidgets.infoDayResources.DateWidget import DateWidget
from customWidgets.infoDayResources.WeatherWidget import WeatherWidget
from customWidgets.infoDayResources.TempWidget import TempWidget
from customWidgets.infoDayResources.ClockWidget import ClockWidget
from kivy.uix.relativelayout import RelativeLayout
from customWidgets.utils.BehaviorUtil import DraggableBaseWidget
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

from kivy.lang import Builder


class InfoDayWidget(DraggableBaseWidget):
    def __init__(self, **kwargs):
        super(InfoDayWidget, self).__init__(**kwargs)
        self.__name__ = "info"
        self.dbName = "infoDay"
        self.size_hint = (.3, .15)
        # self.pos_hint = {"x": 0, "top": 1}
        # self.pos = (0, Window.size[1] - self.height)
        clock = ClockWidget()
        date = DateWidget()
        temp = TempWidget()
        weather = WeatherWidget()

        tempwea = BoxLayout(orientation="horizontal")
        tempwea.add_widget(temp)
        tempwea.add_widget(weather)

        datetemp = BoxLayout(
            orientation="horizontal",
            spacing=30,
            padding=[10, 0, 0, 0],
            size_hint=(1, 0.3))
        datetemp.add_widget(date)
        datetemp.add_widget(tempwea)

        res = BoxLayout(
            orientation="vertical",
            padding=[10, 10, 0, 0],
            spacing=-self.width/4)
        res.add_widget(clock)
        res.add_widget(datetemp)
        self.add_widget(res)
