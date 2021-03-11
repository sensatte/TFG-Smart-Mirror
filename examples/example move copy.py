from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.button import Button

kv = '''
<MyButt>:
    size_hint: None, None
    size: 250, 250
BoxLayout:
    pos_hint: {'top': 1}
    orientation: 'vertical'
    size_hint_y: None
    height: self.minimum_height
    Label:
        text: 'One At A Time'
        size_hint: 1, None
        font_size: 50
        height: 75
        text_size: self.size
        halign: 'center'
    ScrollView:
        size_hint: 1, None
        height: 250
        do_scroll_y: False
        BoxLayout:
            id: box
            size_hint_x: None
            width: self.minimum_width
            orientation: 'horizontal'
            padding: 10
            spacing: 10
'''


class MyButt(Button):
    pass


class TestApp(App):
    def build(self):
        Clock.schedule_once(self.add_buttons)
        return Builder.load_string(kv)

    def add_buttons(self, dt):
        box = self.root.ids.box
        for i in range(25):
            # Add some widgets to the ScrollView
            box.add_widget(MyButt(text='Button ' + str(i)))

TestApp().run()