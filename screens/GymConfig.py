from kivy.uix.screenmanager import ScreenManager, Screen
from kivy_garden.graph import Graph, MeshLinePlot, SmoothLinePlot
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton

from kivy.app import App
from kivy.animation import Animation
from functools import partial
from kivy.uix.screenmanager import FadeTransition

import db.dbWrapper as dbWrapper
from customWidgets.utils.BehaviorUtil import CarouselConfig
import datetime
import operator
import calendar

from kivy.uix.button import Button

#import kv
from kivy.lang import Builder
Builder.load_file('kv\\gymConfig.kv')


class GymConfig(Screen):
    #TODO cronometro? algo para hacer ejercicio
    def __init__(self, **kwargs):
        super(GymConfig, self).__init__(**kwargs)
        self.pos_hint={'center_y': 0.5, 'center_x': 0.5}  
        self.getAllMonth()
        self.getMonthGraph()
        self.add_buttons()

    def create_graph(self, dates):
        if len(dates)>0:
            graph = Graph(x_ticks_minor=5,
                        y_ticks_minor=5, x_ticks_major=5, y_ticks_major=5,
                        y_grid_label=True, x_grid_label=True, padding=5, border_color=[0,0,0,0], font_size=8,
                        xmin=0, xmax=calendar.monthrange(dates[0].year,dates[0].month)[1], ymin=int(min([x.weight for x in dates])-5), ymax=int(max([x.weight for x in dates])+5))
        else:
            graph = Graph(x_ticks_minor=5,
                        y_ticks_minor=5, x_ticks_major=5, y_ticks_major=5,
                        y_grid_label=True, x_grid_label=True, padding=5, border_color=[0,0,0,0], font_size=8,
                        xmin=0, ymin=0)
        
        plot = SmoothLinePlot(color=[1, 105/255, 97/255, 1])
        plot.points = [(x.day, float(x.weight)) for x in dates]
        graph.add_plot(plot)

        return graph


    def getMonthGraph(self):
        datos=dbWrapper.getWeightByMonth(datetime.datetime.today().month)
        self.ids.showNotes.add_widget(self.create_graph(datos))

    def getAllMonth(self):
        datos=dbWrapper.getAllWeight()
        for j in range(len(datos)-1,-1,-1):
            i=datos[j]
            layout= BoxLayout(orientation='horizontal', size_hint_y= None, height= 20)
            layout.add_widget(Label(text=str(i.weight)))
            layout.add_widget(Label(text=str(i.month) + "/" + str(i.day)))
            self.ids.todosgrid.add_widget(layout)

    def add_buttons(self):
        box = self.ids.box
        diez = self.ids.diez
        uni = self.ids.uni
        for i in range(10):
            box.add_widget(CarouselConfig(text=str(i), group="cien", state="down" if i==0 else "normal"))
            diez.add_widget(CarouselConfig(text=str(i)+".", group="diez", state="down" if i==0 else "normal"))
            uni.add_widget(CarouselConfig(text=str(i), group="uni", state="down" if i==0 else "normal"))

    def saveWeight(self):        
        dic={self.ids.box:"0",self.ids.diez:"0",self.ids.uni:"0"}
        
        for grupo in dic:
            for boton in grupo.children:
                if (boton.state=="down"): 
                    dic[grupo]= boton.text
                    break

        peso=float(dic[self.ids.box]+dic[self.ids.diez]+dic[self.ids.uni])
        dbWrapper.saveWeight(peso)
        self.ids.showNotes.remove_widget(self.ids.showNotes.children[0])
        self.getMonthGraph()
        
        for i in range(2, len(self.ids.todosgrid.children)):
            self.ids.todosgrid.remove_widget(self.ids.todosgrid.children[0])
        self.getAllMonth()

    def pressedBack(self, widget):
        anim = Animation(pos_hint={"center_x": .5, "y": -.03}, duration=.1)
        anim += Animation(pos_hint={"center_x": .5, "y": 0}, duration=.1)
        anim.bind(on_complete=partial(self.goToMenuScreen))
        anim.start(widget)
    def goToMenuScreen(self, widget, selected):
        App.get_running_app().root.transition = FadeTransition(duration=.3)
        App.get_running_app().root.current = "menu"

    def goodAnim(self, boton):
        anim = Animation(backgSave=[1,1,1,.5], duration=.1)
        anim += Animation(backgSave=[1,1,1,.2], duration=.1)
        anim.start(boton)

