from mongoengine import Document, StringField, BooleanField, DateTimeField, ObjectIdField, IntField, ListField, FloatField
import datetime


class Notes(Document):
    _id = IntField(required=True)
    title = StringField(required=True, max_length=50)
    pinned = BooleanField(required=True)
    text = StringField(required=True)
    date = DateTimeField(default=datetime.datetime.now)
    rgb = ListField(required=True)


class Counters(Document):
    _id = StringField(required=True, max_length=100)
    cont = IntField(required=True, default=0)


class Gifs(Document):
    _id = IntField(required=True)
    source = StringField(required=True, max_length=200)
    pinned = BooleanField(required=False, default=True)
    posX = FloatField(required=True)
    posY = FloatField(required=True)
    sizeX = FloatField(required=True)
    sizeY = FloatField(required=True)
    rotation = IntField(required=False, default=0)
    delay = FloatField(required=False, default=0.1, precision=2)
