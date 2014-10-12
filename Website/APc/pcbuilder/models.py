from django.db import models

from mongoengine import *
from APc.settings import DBNAME

connect(DBNAME)

class Processor(Document):
    categorie = StringField(max_length=120, required=True)
    naam = StringField(max_length=500, required=True)


'''   subnaam = StringField(max_length=500)
   info = StringField(max_length=500)
   stock = StringField(max_length=500)
   prijs = StringField(max_length=120)




from django.db import models

from mongoengine import *
from django.conf import settings
import logging

logging.info(settings.DBNAME)

result = connect(settings.DBNAME)
logging.info(result)

class Processor(Document):
    categorie = StringField(max_length=120, required=True)
    logging.info(categorie)
    naam = StringField(max_length=500, required=True)
    subnaam = StringField(max_length=500, required=True)
    info = StringField(max_length=500, required=True)
    stock = StringField(max_length=500, required=True)
    prijs = StringField(max_length=120, required=True)
'''