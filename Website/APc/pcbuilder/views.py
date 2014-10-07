from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Processor
import datetime

def index(request):
    # Get all posts from DB
    processoren = Processor.objects 
    return render_to_response('index.html', {'Processoren': processoren},
                              context_instance=RequestContext(request))

def processoren(request):

    # Get all posts from DB
    processoren = Processor.objects(categorie__contains="Processor") 
    return render_to_response('processoren.html', {'Processoren': processoren},
                              context_instance=RequestContext(request))

