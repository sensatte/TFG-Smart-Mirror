from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
Builder.load_string('''
<Box>:
    orientation: 'vertical'
    FloatLayout:
        ScrollView:
            Label:
                id: lab
                size_hint_y: None
                text_size: self.width, None
                text: 'l or emi psum '*100
                height:self.texture_size[1]
    Button:
        size_hint_y: None
        height: 100
        on_release: root.ids.lab.text+='lo rem '*100
''')
class Box(BoxLayout): pass
class My(App):
    def build(self):
        return Box()
My().run()