from kivy.uix.screenmanager import ScreenManager, Screen
from kivy_garden.graph import Graph, MeshLinePlot, SmoothLinePlot

from kivy.app import App
from kivy.animation import Animation
from functools import partial
from kivy.uix.screenmanager import FadeTransition

import db.dbWrapper as dbWrapper
import datetime
import operator
import calendar

#import kv
from kivy.lang import Builder
Builder.load_file('kv\\gymConfig.kv')


class GymConfig(Screen):
    #TODO cronometro? algo para hacer ejercicio
    #TODO boton añadir peso cuidao que no exista ya uno
    #TODO mostrar vista año
    def __init__(self, **kwargs):
        super(GymConfig, self).__init__(**kwargs)
        self.pos_hint={'center_y': 0.5, 'center_x': 0.5}       

        self.getMonthGraph()


    def create_graph(self, dates):
        graph = Graph(x_ticks_minor=5,
                    y_ticks_minor=5, x_ticks_major=5, y_ticks_major=5,
                    y_grid_label=True, x_grid_label=True, padding=5, border_color=[0,0,0,0], font_size=8,
                    xmin=0, xmax=calendar.monthrange(dates[0].year,dates[0].month)[1], ymin=int(min([x.weight for x in dates])-5), ymax=int(max([x.weight for x in dates])+5))
        plot = SmoothLinePlot(color=[1, 105/255, 97/255, 1])
        plot.points = [(x.day, float(x.weight)) for x in dates]
        graph.add_plot(plot)

        return graph


    def getMonthGraph(self):
        datos=dbWrapper.getWeightByMonth(datetime.datetime.today().month)
        self.ids.mes.add_widget(self.create_graph(datos))


    def pressedBack(self, widget):
        anim = Animation(pos_hint={"center_x": .5, "y": -.03}, duration=.1)
        anim += Animation(pos_hint={"center_x": .5, "y": 0}, duration=.1)
        anim.bind(on_complete=partial(self.goToMenuScreen))
        anim.start(widget)
    def goToMenuScreen(self, widget, selected):
        App.get_running_app().root.transition = FadeTransition(duration=.3)
        App.get_running_app().root.current = "menu"
