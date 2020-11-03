import kivy
kivy.require('1.11.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from customWidgets.NewsWidget import NewsWidget
from customWidgets.ClockWidget import ClockWidget
from customWidgets.RootLayout import RootLayout
from customWidgets.DateWidget import DateWidget
from customWidgets.WeatherWidget import WeatherWidget
from customWidgets.TempWidget import TempWidget

import threading
from gpio_translator import gpio_translate
  
class SmartMirrorApp(App):
      
    def build(self):
        
        
        widgets = []
        
        news_widget = NewsWidget()
        widgets.append(news_widget)

        clock = ClockWidget()  
        widgets.append(clock)

        date = DateWidget()  
        widgets.append(date)

        weather = WeatherWidget()  
        widgets.append(weather)

        temp = TempWidget()  
        widgets.append(temp)
        
        sad_cat = Image(source="images/imageFile.jpeg",
                        allow_stretch=True, keep_ratio=False,
                        size_hint =(.1, .1),
                        pos_hint ={"x":0.1, "y":0.1}
                        )
        widgets.append(sad_cat)
        
        patata = Label(text="Patata")
        widgets.append(patata)
        
        root_layout = RootLayout()
        
        for widget in widgets:
            root_layout.add_widget(widget)
                
        return root_layout
  
  
if __name__ == '__main__':

    #GPIO to Keyboard Translate
    gpio_translate_thread = threading.Thread(target=gpio_translate, name='GPIO Translation')
    gpio_translate_thread.daemon = True
    gpio_translate_thread.start()
    
    SmartMirrorApp().run()
