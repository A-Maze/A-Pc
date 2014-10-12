from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Processoren
import logging

def index(request):
    # Get all posts from DB
    processoren = Processoren.objects
    return render_to_response('index.html', {'Processoren': processoren},
                              context_instance=RequestContext(request))



def processoren(request):

    # Get all posts from DB
    processoren = Processoren.objects[:5]
    return render_to_response('processoren.html', {'Processoren': processoren},
                              context_instance=RequestContext(request))

