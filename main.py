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
import webbrowser
import threading

kivy.require('2.0.0')

# Window.size = (1280, 720)

Window.fullscreen = "auto"

# Window.size = (540, 760)

Window.minimum_width, Window.minimum_height = Window.size


class SmartMirrorApp(App):

    def build(self):

        Config.set("kivy", "keyboard_mode", "systemanddock")
        Config.write()

        # Create the screen manager
        scMenu = ScreenManager()

        home = HomeScreen(name="home")
        scMenu.add_widget(home)

        menu = MenuScreen(name="menu")
        scMenu.add_widget(menu)

        settings = Screen(name="gallery")
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

        scMenu.current = "gym"

        self.set_keyboard()

        return scMenu

    def set_keyboard(self):
        VKeyboard.key_background_normal = "images/keyboard/normal.png"
        VKeyboard.key_background_down = "images/keyboard/down.png"
        VKeyboard.background = "images/keyboard/transparent.png"

def minimizeSpotify():
    try:

        import gi                         #Import gi pageage
        gi.require_version('Wnck','3.0')
        from gi.repository import Wnck    #Import Wnck module

        screen=Wnck.Screen.get_default()  #Get screen information
        screen.force_update()             #Update screen object
        windows=screen.get_windows()      #Get all windows in task bar. The first 2 elements I believe relate to the OS GUI interface itself and the task bar. All other elements are the open windows in the task bar in that order.
        print("WINDOWES")
        while True:
            for w in windows:                #Go through each window one by one.
                if 'Spotify' in w.get_name(): #Get name of window and check if it includes 'Chromium'
                    w.minimize()
                    print("minimized spotify")
                    return              #If so, minimize ask the task manager to minimize that window.

    except:
        pass

if __name__ == '__main__':

    webbrowser.open("https://open.spotify.com")

    #t = threading.Thread(name='minimize_spotify', target=minimizeSpotify)

    #t.start()


    # GPIO to Keyboard Translate
    # gpio_translate_thread = threading.Thread(target=gpio_translate, name='GPIO Translation')
    # gpio_translate_thread.daemon = True
    # gpio_translate_thread.start()

    SmartMirrorApp().run()
