from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import loader
from models import Processoren
import logging
import json

def index(request):
    # Get all posts from DB
    processoren = Processoren.objects
    return render_to_response('index.html', {'Processoren': processoren},
                              context_instance=RequestContext(request))



def processoren(request):

    # Get all posts from DB
    processoren = Processoren.objects.filter(categorie__contains='Processor')[:10]
    #processoren = json.dumps(list(uniArray))
    return render_to_response('processoren.html', {'Processoren': processoren},
                              context_instance=RequestContext(request))

def behuizingen(request):

    # Get all posts from DB
    processoren = Processoren.objects(categorie__contains='Behuizing')[:10]
    return render_to_response('behuizing.html', {'Processoren': processoren},
                              context_instance=RequestContext(request))

def geheugen(request):

    # Get all posts from DB
    processoren = Processoren.objects(categorie__contains='Geheugen')[:10]
    return render_to_response('geheugen.html', {'Processoren': processoren},
                              context_instance=RequestContext(request))

def gpu(request):

    # Get all posts from DB
    processoren = Processoren.objects(categorie__contains='Grafische kaarten')[:10]
    return render_to_response('gpu.html', {'Processoren': processoren},
                              context_instance=RequestContext(request))

def hardeschijf(request):

    # Get all posts from DB
    processoren = Processoren.objects(categorie__contains='Harde schijven')[:10]
    return render_to_response('hardeschijf.html', {'Processoren': processoren},
                              context_instance=RequestContext(request))

def koeling(request):

    # Get all posts from DB
    processoren = Processoren.objects(categorie__contains='Koeling')[:10]
    return render_to_response('koeling.html', {'Processoren': processoren},
                              context_instance=RequestContext(request))

def moederborden(request):

    # Get all posts from DB
    processoren = Processoren.objects(categorie__contains='Moederborden')[:10]
    return render_to_response('moederbord.html', {'Processoren': processoren},
                              context_instance=RequestContext(request))

def optischeschijf(request):

    # Get all posts from DB
    processoren = Processoren.objects(categorie__contains='DVD, Blu-ray & backup')[:10]
    return render_to_response('optischeschijf.html', {'Processoren': processoren},
                              context_instance=RequestContext(request))

def voedingen(request):

    # Get all posts from DB
    processoren = Processoren.objects(categorie__contains='Voedingen')[:10]
    return render_to_response('voeding.html', {'Processoren': processoren},
                              context_instance=RequestContext(request))





