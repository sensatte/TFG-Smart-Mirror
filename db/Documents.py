from mongoengine import Document, StringField, BooleanField, DateTimeField, ObjectIdField, IntField, ListField
import datetime

class Notes(Document):
    _id= IntField(required=True)
    title = StringField(required=True, max_length=50)
    pinned = BooleanField(required= True)
    text = StringField(required=True)
    date = DateTimeField(default=datetime.datetime.now)
    rgb = ListField(required=True)

class Counters(Document):
    _id = StringField(required=True, max_length=100)
    cont = IntField(required=True, default=0)