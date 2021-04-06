from mongoengine import Document, DecimalField, ObjectIdField, StringField, BooleanField, DateTimeField, ObjectIdField, IntField, ListField, FloatField
import datetime


class Notes(Document):
    _id = IntField(required=True)
    pinned = BooleanField(required=True)
    text = StringField(required=True)
    date = DateTimeField(default=datetime.datetime.now)
    rgb = ListField(required=True)

    scale = FloatField(required=False, default=1)
    rotation = FloatField(required=False, default=0)
    sizeX = FloatField(required=False, default=.15)
    sizeY = FloatField(required=False, default=.15)
    posX = FloatField(required=False, default=20)
    posY = FloatField(required=False, default=20)

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
    source = StringField(required=True, max_length=500)
    pinned = BooleanField(required=False, default=True)
    posX = FloatField(required=True)
    posY = FloatField(required=True)
    sizeX = FloatField(required=False)
    sizeY = FloatField(required=False)
    scale = FloatField(required=False, default=1)
    rotation = IntField(required=False, default=0)
    delay = FloatField(required=False, default=0.1, precision=2)


class Gym(Document):
    year = IntField(required=True)
    month = IntField(required=True)
    day = IntField(required=True)
    weight = DecimalField(required=True)


class Draggable(Document):
    draggableName = StringField(required=True, max_length=500)
    posX = FloatField(required=False, default=50)
    posY = FloatField(required=False, default=50)
