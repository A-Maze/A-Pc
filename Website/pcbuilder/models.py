from django.db import models

from mongoengine import *
from APc.settings import DBNAME

connect(DBNAME)

class Moederborden(Document):
    categorie = StringField(max_length=120)
    naam = StringField(max_length=500)
    subnaam = StringField(max_length=500)
    info = StringField(max_length=500)
    stock = StringField(max_length=500)
    prijs = StringField(max_length=120)

class Processoren(Document):
    categorie = StringField(max_length=120)
    naam = StringField(max_length=500)
    subnaam = StringField(max_length=500)
    info = StringField(max_length=500)
    stock = StringField(max_length=500)
    prijs = StringField(max_length=120)

class Koeling(Document):
    categorie = StringField(max_length=120)
    naam = StringField(max_length=500)
    subnaam = StringField(max_length=500)
    info = StringField(max_length=500)
    stock = StringField(max_length=500)
    prijs = StringField(max_length=120)

class Behuizingen(Document):
    categorie = StringField(max_length=120)
    naam = StringField(max_length=500)
    subnaam = StringField(max_length=500)
    info = StringField(max_length=500)
    stock = StringField(max_length=500)
    prijs = StringField(max_length=120)

class Grafische(Document):
    categorie = StringField(max_length=120)
    naam = StringField(max_length=500)
    subnaam = StringField(max_length=500)
    info = StringField(max_length=500)
    stock = StringField(max_length=500)
    prijs = StringField(max_length=120)

class Harde(Document):
    categorie = StringField(max_length=120)
    naam = StringField(max_length=500)
    subnaam = StringField(max_length=500)
    info = StringField(max_length=500)
    stock = StringField(max_length=500)
    prijs = StringField(max_length=120)

class Dvd(Document):
    categorie = StringField(max_length=120)
    naam = StringField(max_length=500)
    subnaam = StringField(max_length=500)
    info = StringField(max_length=500)
    stock = StringField(max_length=500)
    prijs = StringField(max_length=120)

class Geheugen(Document):
    categorie = StringField(max_length=120)
    naam = StringField(max_length=500)
    subnaam = StringField(max_length=500)
    info = StringField(max_length=500)
    stock = StringField(max_length=500)
    prijs = StringField(max_length=120)

class Voeding(Document):
    categorie = StringField(max_length=120)
    naam = StringField(max_length=500)
    subnaam = StringField(max_length=500)
    info = StringField(max_length=500)
    stock = StringField(max_length=500)
    prijs = StringField(max_length=120)
