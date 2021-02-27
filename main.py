from screens.MenuScreen import MenuScreen
from kivy.lang import Builder
from screens.InfoDayConfig import InfoDayConfig
from screens.HomeScreen import HomeScreen
from screens.NotesConfig import NotesConfig
from kivy.uix.screenmanager import FadeTransition, RiseInTransition, ScreenManager, Screen
from kivy.core.window import Window
from kivy.app import App
import kivy
kivy.require('2.0.0')  # replace with your current kivy version !

Window.size = (540, 700)
# Window.size = (540, 960)
Window.minimum_width, Window.minimum_height = Window.size
class SmartMirrorApp(App):

    def build(self):

        #TODO es probable que pasen las mierdas de las screens negras y 
        # no transparentes porque metemos las screens dentro de las screens
        #TODO forma bonita de meter las pantallas
        #TODO que se puedan borrar las notas
        # Create the screen manager
        scMenu = ScreenManager()

        home = HomeScreen(name="home")
        scMenu.add_widget(home)

        menu = MenuScreen(name="menu")
        scMenu.add_widget(menu)

        infoDay = Screen(name="clock")
        infoDay.add_widget(InfoDayConfig())
        scMenu.add_widget(infoDay)
        
        notes = Screen(name="notes")
        notes.add_widget(NotesConfig())
        scMenu.add_widget(notes)

        scMenu.current = "notes"

        return scMenu


if __name__ == '__main__':

    # GPIO to Keyboard Translate
    # gpio_translate_thread = threading.Thread(target=gpio_translate, name='GPIO Translation')
    # gpio_translate_thread.daemon = True
    # gpio_translate_thread.start()

    SmartMirrorApp().run()
