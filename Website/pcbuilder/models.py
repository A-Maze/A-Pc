from django.db import models

from mongoengine import *
from APc.settings import DBNAME
from django import forms
from django.forms import PasswordInput

connect(DBNAME)

class Login(forms.Form):
    email = forms.CharField(max_length=100, required=True)
    wachtwoord = forms.CharField(max_length=20 ,required=True, widget=PasswordInput())

class Registreer(forms.Form):
    voornaam = forms.CharField(max_length=100, required=True)
    achternaam = forms.CharField(max_length=100, required=True)
    email = forms.CharField(max_length=100, required=True)
    wachtwoord = forms.CharField(max_length=20 ,required=True, widget=PasswordInput())
    Herhaal_wachtwoord = forms.CharField(max_length=20 ,required=True, widget=PasswordInput())

class Users(Document):
    Voornaam = StringField(max_length=500)
    Achternaam = StringField(max_length=500)
    Email = StringField(max_length=500)
    Wachtwoord = StringField(max_length=500)
    Rechten = StringField(max_length=500)

class Views(Document):

    Id = StringField(max_length=500)
    Categorie = StringField(max_length=500)
    Aantal = StringField(max_length=50)

class ViewsPerDatum(Document):
    Aantal = StringField(max_length=500)
    Datum = StringField(max_length=50)

class SearchQuery(Document):
    Zoekwoord = StringField(max_length=500)
    Aantal = StringField(max_length=500)

class Select(Document):

    Id = StringField(max_length=500)
    Categorie = StringField(max_length=500)
    Aantal = StringField(max_length=50)

class Moederborden(Document):
    
    categorie = StringField(max_length=120)
    Product = StringField(max_length=500)
    Uitvoering = StringField(max_length=500)
    Hardeschijf_bus = StringField(max_length=500)
    info = StringField(max_length=500)
    stock = StringField(max_length=500)
    prijs = StringField(max_length=120)
    Afbeelding = StringField(max_length=500)
    ean = StringField(max_length=200)
    sku = StringField(max_length=200)
    herkomst = StringField(max_length=200)  
    link = StringField(max_length=200)
class Processoren(Document):
    
    herkomst = StringField(max_length=200)
    categorie = StringField(max_length=120)
    Uitvoering = StringField(max_length=500)
    naam = StringField(max_length=500)
    subnaam = StringField(max_length=500)
    info = StringField(max_length=500)
    prijs = StringField(max_length=120)
    stock = StringField(max_length=500)
    
    ean = StringField(max_length=200)
    sku = StringField(max_length=200)
    herkomst = StringField(max_length=200)  
    link = StringField(max_length=200)


class Koeling(Document):
    
    categorie = StringField(max_length=120)
    naam = StringField(max_length=500)
    Uitvoering = StringField(max_length=500)
    subnaam = StringField(max_length=500)
    info = StringField(max_length=500)
    stock = StringField(max_length=500)
    prijs = StringField(max_length=120)
    ean = StringField(max_length=200)
    sku = StringField(max_length=200)
    herkomst = StringField(max_length=200)  
    link = StringField(max_length=200)

class Behuizingen(Document):
    
    categorie = StringField(max_length=120)
    Product = StringField(max_length=500)
    Behuizingtype = StringField(max_length=500)
    Uitvoering = StringField(max_length=500)
    info = StringField(max_length=500)
    stock = StringField(max_length=500)
    prijs = StringField(max_length=120)
    Afbeelding = StringField(max_length=500)
    ean = StringField(max_length=200)
    sku = StringField(max_length=200)
    herkomst = StringField(max_length=200)  
    link = StringField(max_length=200)

class Grafische(Document):
    
    categorie = StringField(max_length=120)
    naam = StringField(max_length=500)
    subnaam = StringField(max_length=500)
    Uitvoering = StringField(max_length=500)
    info = StringField(max_length=500)
    stock = StringField(max_length=500)
    prijs = StringField(max_length=120)
    ean = StringField(max_length=200)
    sku = StringField(max_length=200)
    herkomst = StringField(max_length=200)  
    link = StringField(max_length=200)

class Harde(Document):
    
    categorie = StringField(max_length=120)
    naam = StringField(max_length=500)
    subnaam = StringField(max_length=500)
    Uitvoering = StringField(max_length=500)
    info = StringField(max_length=500)
    stock = StringField(max_length=500)
    prijs = StringField(max_length=120)
    ean = StringField(max_length=200)
    sku = StringField(max_length=200)
    herkomst = StringField(max_length=200)  
    link = StringField(max_length=200)

class Dvd(Document):
    
    categorie = StringField(max_length=120)
    naam = StringField(max_length=500)
    subnaam = StringField(max_length=500)
    Uitvoering = StringField(max_length=500)
    info = StringField(max_length=500)
    stock = StringField(max_length=500)
    prijs = StringField(max_length=120)
    ean = StringField(max_length=200)
    sku = StringField(max_length=200)
    herkomst = StringField(max_length=200)  
    link = StringField(max_length=200)

class Geheugen(Document):
    
    categorie = StringField(max_length=120)
    naam = StringField(max_length=500)
    Merk = StringField(max_length=500)
    Uitvoering = StringField(max_length=500)
    Geheugen_Specificatie = StringField(max_length=500)
    Afbeelding = StringField(max_length=500)
    info = StringField(max_length=500)
    stock = StringField(max_length=500)
    prijs = StringField(max_length=120)
    ean = StringField(max_length=200)
    sku = StringField(max_length=200)
    herkomst = StringField(max_length=200)  
    link = StringField(max_length=200)

class Voeding(Document):
    
    categorie = StringField(max_length=120)
    naam = StringField(max_length=500)
    subnaam = StringField(max_length=500)
    Uitvoering = StringField(max_length=500)
    info = StringField(max_length=500)
    stock = StringField(max_length=500)
    prijs = StringField(max_length=120)
    ean = StringField(max_length=200)
    sku = StringField(max_length=200)
    herkomst = StringField(max_length=200)  
    link = StringField(max_length=200)
