import re
import urllib.request
import json
from bs4 import BeautifulSoup
import requests
import datetime

from kivy.uix.label import Label
import db.dbWrapper as dbWrapper
from kivy.uix.image import Image
import kivy.properties as Properties


class InternationalWidget(Image):
    # TODO mirar si cuando es un dia <10 no de problemas
    # TODO se actualizara?
    text = Properties.StringProperty('')
    chosenColor = Properties.ListProperty()

    def on_text(self, *_):
        # Just get large texture:
        l = Label(text=self.text)
        l.font_size = '1000dp'  # something that'll give texture bigger than phone's screen size
        l.color = self.color
        l.texture_update()
        # Set it to image, it'll be scaled to image size automatically:
        self.texture = l.texture

    def __init__(self, **kwargs):
        super(InternationalWidget, self).__init__(**kwargs)
        self.chosenColor = dbWrapper.getInternacionalByID().color
        self.size_hint = (1, .2)
        hoy = dbWrapper.getInternacionalByDay(
            datetime.date.today().strftime('%d/%m'))
        self.text = hoy[0]['info'] if len(
            hoy) != 0 else "Día Mundial del Teatro"
        self.color = self.chosenColor if len(hoy) != 0 else [1, 1, 1, 1]

# --------------------------------


    def readPage(self):
        meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
                 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre', ]

        internacionales = list()

        for mes in range(len(meses)):
            page = requests.get(
                "https://www.diainternacionalde.com/mes/" + meses[mes])
            soup = BeautifulSoup(page.content, 'html.parser')
            dias = soup.find_all("article", {"class": "dia"})

            for v in dias:
                lista = list()
                dia = int(v.find("span").text.split(" ")[0])
                try:
                    info = v.find("a").text
                except:
                    info = v.find("h3").text

                lista.append(
                    str(dia)+'/'+(str(mes+1) if mes >= 10 else '0'+str(mes+1)))
                lista.append(str(mes+1) if mes >= 10 else '0'+str(mes+1))
                lista.append(info)
                if lista not in internacionales:
                    internacionales.append(lista)

        return internacionales

    def almacenar_bd(self):
        internacionales = self.readPage()
        for inter in internacionales:
            dbWrapper.saveInternacional(inter[0], inter[1], inter[2])


class LabelAjustado(Label):
    def __init__(self, text, colorb, max, **kwargs):
        super(LabelAjustado, self).__init__(**kwargs)
        self.text = text
        self.colorb = colorb
        self.max = max
