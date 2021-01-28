from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

kv_file = '''
<MyButton@Button>:
    color: .8,.9,0,1
    font_size: 32

<KVMyHBoxLayout>:
    orientation: 'vertical'
    MyButton:
        id:"idBtn1"
        text: "Btn1"
        background_color: 1,0,0,1
        on_press:app.Pressbtn(self)
    MyButton:
        id:"idBtn2"
        text: "Btn2"
        background_color: 0,1,0,1
        on_press:app.Pressbtn(self)
    Label:
        id: lobj
        text: "Object"
        background_color: 1,0,1,1

    Label:
        id: lid
        text: "ID"
        background_color: 0,0,1,1
    Label:
        id: ltext
        text: "Text"
        background_color: 1,0,1,1
'''


class KVMyHBoxLayout(BoxLayout):
    pass

class ExampleApp(App):
    def Pressbtn(self, instance):
        instance.parent.ids.lobj.text = str(instance)
        instance.parent.ids.ltext.text = instance.text
        instance.parent.ids.lid.text= self.get_id(instance)

    def get_id(self,  instance):
        for id, widget in instance.parent.ids.items():
            if widget.__self__ == instance:
                return id

    def build(self):
        Builder.load_string(kv_file)
        return KVMyHBoxLayout()

if __name__ == "__main__":
    app = ExampleApp()
    app.run()