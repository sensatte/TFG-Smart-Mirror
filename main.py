import kivy
kivy.require('2.0.0')  # replace with your current kivy version !

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

from screens.Home import Home
from screens.MenuLayout import MenuLayout
from screens.InfoDayConfig import InfoDayConfig

Window.size = (540,960)
Window.minimum_width, Window.minimum_height = Window.size

#import kv
from kivy.lang import Builder
Builder.load_file('kv\\main.kv')

class SmartMirrorApp(App):

    def build(self):

        #TODO forma bonita de meter las pantallas
        # Create the screen manager
        scMenu=ScreenManager()
        
        home = Screen(name="home")
        home.add_widget(Home())
        scMenu.add_widget(home)

        menu=Screen(name="menu")
        menu.add_widget(MenuLayout())
        scMenu.add_widget(menu)

        infoDay=Screen(name="clock")
        infoDay.add_widget(InfoDayConfig())
        scMenu.add_widget(infoDay)

        scMenu.current = "clock"
        
        return scMenu


if __name__ == '__main__':

    #GPIO to Keyboard Translate
    # gpio_translate_thread = threading.Thread(target=gpio_translate, name='GPIO Translation')
    # gpio_translate_thread.daemon = True
    # gpio_translate_thread.start()
    
    SmartMirrorApp().run()
