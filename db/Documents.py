from mongoengine import Document, StringField, BooleanField, DateTimeField, ObjectIdField, IntField
import datetime

class Notes(Document):
    _id= IntField(required=True)
    title = StringField(required=True, max_length=50)
    pinned = BooleanField(required= True)
    text = StringField(required=True)
    date = DateTimeField(default=datetime.datetime.now)
    r = StringField(required=True, max_length=3)
    g = StringField(required=True, max_length=3)
    b = StringField(required=True, max_length=3)

class Counters(Document):
    _id = StringField(required=True, max_length=100)
    cont = IntField(required=True, default=0)