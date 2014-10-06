from django.db import models

from mongoengine import *
from APc.settings import DBNAME

connect(DBNAME)

class Processoren(Document):
    prijs = StringField(max_length=120, required=True)
    categorie = StringField(max_length=500, required=True)
    titel = StringField(max_length=500, required=True)
    image = StringField(max_length=500, required=True)
    omschrijving = StringField(max_length=500, required=True)