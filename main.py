from screens.GifsConfig import GifsConfig
from screens.MenuScreen import MenuScreen
from kivy.lang import Builder
from screens.InfoDayConfig import InfoDayConfig
from screens.InternationalConfig import InternationalConfig
from screens.SpotifyConfig import SpotifyConfig
from screens.SaveScreen import SaveScreen
from screens.SettingsScreen import SettingsScreen
from screens.QuotesConfig import QuotesConfig
from screens.GymConfig import GymConfig
from screens.HomeScreen import HomeScreen
from screens.TwitterConfig import TwitterConfig
from screens.DrawingScreen import DrawingScreen
from screens.NotesConfig import NotesConfig
from kivy.uix.screenmanager import FadeTransition, RiseInTransition, ScreenManager, Screen
from kivy.core.window import Window
from kivy.app import App
import kivy
from kivy.uix.vkeyboard import VKeyboard
from kivy.config import Config
kivy.require('2.0.0')

#Window.size = (1280, 720)
# Window.borderless = True
# Window.left = 0
# Window.top = 0

Window.fullscreen = "auto"

Window.on_minimize = Window.maximize

# Window.size = (540, 760)

Window.minimum_width, Window.minimum_height = Window.size


class SmartMirrorApp(App):

    def build(self):

        # TODO es probable que pasen las mierdas de las screens negras y
        # no transparentes porque metemos las screens dentro de las screens
        # TODO forma bonita de meter las pantallas

        Config.set("kivy", "keyboard_mode", "systemanddock")
        Config.write()

        # Create the screen manager
        scMenu = ScreenManager()

        home = HomeScreen(name="home")
        scMenu.add_widget(home)

        menu = MenuScreen(name="menu")
        scMenu.add_widget(menu)

        settings = Screen(name="settings")
        settings.add_widget(SettingsScreen())
        scMenu.add_widget(settings)

        infoDay = Screen(name="clock")
        infoDay.add_widget(InfoDayConfig())
        scMenu.add_widget(infoDay)

        save = SaveScreen(name="save")
        scMenu.add_widget(save)

        notes = Screen(name="notes")
        notes.add_widget(NotesConfig())
        scMenu.add_widget(notes)

        spotify = Screen(name="spotify")
        spotify.add_widget(SpotifyConfig())
        scMenu.add_widget(spotify)

        gym = Screen(name="gym")
        gym.add_widget(GymConfig())
        scMenu.add_widget(gym)

        inter = Screen(name="international")
        inter.add_widget(InternationalConfig())
        scMenu.add_widget(inter)

        drawing = Screen(name="drawing")
        drawing.add_widget(DrawingScreen())
        scMenu.add_widget(drawing)

        twitter = Screen(name="twitter")
        twitter.add_widget(TwitterConfig())
        scMenu.add_widget(twitter)

        gifs = Screen(name="gifs")
        gifs.add_widget(GifsConfig())
        scMenu.add_widget(gifs)

        quotes = Screen(name="quotes")
        quotes.add_widget(QuotesConfig())
        scMenu.add_widget(quotes)

        scMenu.current = "home"

        self.set_keyboard()

        Window.maximize()

        return scMenu

    def set_keyboard(self):
        VKeyboard.key_background_normal = "images/keyboard/normal.png"
        VKeyboard.key_background_down = "images/keyboard/down.png"
        VKeyboard.background = "images/keyboard/transparent.png"


if __name__ == '__main__':

    # GPIO to Keyboard Translate
    # gpio_translate_thread = threading.Thread(target=gpio_translate, name='GPIO Translation')
    # gpio_translate_thread.daemon = True
    # gpio_translate_thread.start()

    SmartMirrorApp().run()
