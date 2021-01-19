from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.behaviors import FocusBehavior

# This is a Button that also has focus behavior
class FocusButton(FocusBehavior, Button):
    first_focus = BooleanProperty(False)

    def on_parent(self, widget, parent):
        # if first_focus is set, this Button takes the focus first
        if self.first_focus:
            self.focus = True


class MyPopup(Popup):
    def keydown(self, window, scancode, what, text, modifiers):
        if scancode == 13:
            for w in self.walk():
                if isinstance(w, FocusButton) and w.focus:
                    w.dispatch('on_press')

    def keyup(self, key, scancode, codepoint):
        if scancode == 13:
            for w in self.walk():
                if isinstance(w, FocusButton) and w.focus:
                    w.dispatch('on_release')

    def on_dismiss(self):
        Window.unbind(on_key_down=self.keydown)
        Window.unbind(on_key_up=self.keyup)

Builder.load_string('''
# provide for a small border that indicates Focus
<FocusButton>:
    canvas.before:
        Color:
            rgba: 1,1,1,1
        Rectangle:
            pos: self.x-2, self.y-2
            size: (self.size[0]+4, self.size[1]+4) if self.focus else (0,0)
''')


class testWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        def yes_btn(instance):
            print("this function is called.")

        contents = BoxLayout(orientation='vertical')
        content_text = Label(text="Lanjutkan Transaksi?")
        pop_btn = BoxLayout(spacing=10)

        # set first_focus to True for this Button
        self.btn_yes = FocusButton(text='Ya', size_hint_y=None, height=40, first_focus=True)
        self.btn_no = FocusButton(text='Tidak', size_hint_y=None, height=40)
        pop_btn.add_widget(self.btn_yes)
        pop_btn.add_widget(self.btn_no)
        contents.add_widget(content_text)
        contents.add_widget(pop_btn)

        pop_insert = MyPopup(title="Confirmation Message", content=contents, size_hint=(None, None), size=(300, 300))

        self.btn_yes.bind(on_release=yes_btn)
        self.btn_no.bind(on_release=pop_insert.dismiss)

        # bind to get key down and up events
        Window.bind(on_key_down=pop_insert.keydown)
        Window.bind(on_key_up=pop_insert.keyup)

        pop_insert.open()

class testApp(App):
    def build(self):
        return testWindow()


if __name__ == '__main__':
    m = testApp()
    m.run()