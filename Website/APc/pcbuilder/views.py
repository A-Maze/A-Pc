from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Processor
import logging
from pprint import pprint

def index(request):
    # Get all posts from DB
    processoren = Processor.objects 
    return render_to_response('index.html', {'Processoren': processoren},
                              context_instance=RequestContext(request))

def processoren(request):

    # Get all posts from DB
    processoren = Processor()
    logging.info(type(processoren))
    pprint(vars(processoren))
    #processoren = Processor.objects(categorie__contains="Processor")
    #logging.info(processoren)
    return render_to_response('processoren.html', {'Processoren': processoren},
                              context_instance=RequestContext(request))




'''
 return render_to_response('processoren.html', {'Processoren': processoren},
                              context_instance=RequestContext(request))



    logging.info(processoren.naam('Upgrade Kit ASUS MAXIMUS VI HERO / i7 4770K / 8GB'))


'''