from mongoengine import Document, StringField, BooleanField, DateTimeField, ObjectIdField, IntField, ListField, FloatField
import datetime


class Notes(Document):
    _id = IntField(required=True)
    pinned = BooleanField(required=True)
    text = StringField(required=True)
    date = DateTimeField(default=datetime.datetime.now)
    rgb = ListField(required=True)


class Counters(Document):
    _id = StringField(required=True, max_length=100)
    cont = IntField(required=True, default=0)

class Hora(Document):
    _id = StringField(required=True, max_length=100)
    color = ListField(required=True)
    formato = ListField(required=True)

class Fecha(Document):
    _id = StringField(required=True, max_length=100)
    color = ListField(required=True)
    formato = StringField(required=True)

class Temp(Document):
    _id = StringField(required=True, max_length=100)
    color = ListField(required=True)
    formato = StringField(required=True)

class Clima(Document):
    _id = StringField(required=True, max_length=100)
    formato = StringField(required=True)

class Gifs(Document):
    _id = IntField(required=True)
    name = StringField(required=False, max_length=200)
    source = StringField(required=True, max_length=200)
    pinned = BooleanField(required=False, default=True)
    posX = FloatField(required=True)
    posY = FloatField(required=True)
    sizeX = FloatField(required=True)
    sizeY = FloatField(required=True)
    rotation = IntField(required=False, default=0)
    delay = FloatField(required=False, default=0.1, precision=2)
