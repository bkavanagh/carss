__author__ = 'brendan'
from peewee import *
from datetime import datetime

db = SqliteDatabase('carss.db')

class Car(Model):
    title = CharField()
    description = CharField()
    mileage = CharField()
    year = CharField()
    link = CharField()
    price = CharField()
    location = CharField()
    engine = CharField(null=True)
    fuel = CharField(null=True)
    ref = CharField(unique=True)
    thumb = CharField(null=True)
    updated = DateTimeField(default=datetime.now())

    class Meta:
        database = db

db.connect()
db.create_tables([Car], safe=True)