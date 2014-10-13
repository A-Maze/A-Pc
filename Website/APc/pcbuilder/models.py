from django.db import models

from mongoengine import *
from APc.settings import DBNAME

connect(DBNAME)

class Processoren(Document):
    categorie = StringField(max_length=120)
    naam = StringField(max_length=500)
    subnaam = StringField(max_length=500)
    info = StringField(max_length=500)
    stock = StringField(max_length=500)
    prijs = StringField(max_length=120)


