# pylint: disable=no-member

from kivy.uix.checkbox import CheckBox
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.label import Label

from customWidgets.infoDayResources.DateWidget import DateWidget
from customWidgets.infoDayResources.WeatherWidget import WeatherWidget
from customWidgets.infoDayResources.TempWidget import TempWidget
from customWidgets.infoDayResources.ClockWidget import ClockWidget

#import kv
from kivy.lang import Builder
Builder.load_file('kv\\configs.kv')

class InfoDayConfig(Screen):
    # #TODO hacer el kv que se pueda usar pa mas gente
    #TODO color picker
    def __init__(self, **kwargs):
        super(InfoDayConfig, self).__init__(**kwargs)
        self.pos_hint={'center_y': 0.5, 'center_x': 0.5}


    def secondsClock(self, checkboxInstance):
        if checkboxInstance.text=="Sí":
            ClockWidget.seconds=True
            print("Segundos activados")
        elif checkboxInstance.text=="No":
            ClockWidget.seconds=False
            print("Segundos desactivados")

    def colorClock(self, checkboxInstance):
        ClockWidget.chosenColor = checkboxInstance.color
        print("Color cambiado a ", checkboxInstance.color)

    def formatClock(self, checkboxInstance):
        if checkboxInstance.text=="12h":
            ClockWidget.formato="12h"
            print("Formato: 12h")
        elif checkboxInstance.text=="24h":
            ClockWidget.formato="24h"
            print("Formato: 24h")














        # # Add checkbox, Label and Widget 
        # self.add_widget(Label(text ='Male')) 
        # self.active = CheckBox(active = True) 
        # self.add_widget(self.active) 
  
        # # Adding label to scrren  
        # self.lbl_active = Label(text ='Checkbox is on') 
        # self.add_widget(self.lbl_active) 
          
  
        # # Attach a callback 
        # self.active.bind(active = self.on_checkbox_Active) 
  
   
    # Callback for the checkbox 
    # def on_checkbox_Active(self, checkboxInstance, isActive): 
        # if isActive: 
        #     self.lbl_active.text ="Checkbox is ON"
        #     print("Checkbox Checked") 
        # else: 
        #     self.lbl_active.text ="Checkbox is OFF"
            # print("Checkbox unchecked") 

class Scrolling(ScrollView):
    pass