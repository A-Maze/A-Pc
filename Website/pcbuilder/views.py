from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.template import loader
from models import Processoren
import logging
import json

# Global vars

# Strandaard aantal per pagina
#end = 25
#start = 0
#sl = "0:%d" % (end)
#Dit bovenstaande is voor later om alleen de div te veranderen en niet de hele pagina
app = 15

def index(request):
    # Get all posts from DB
    processoren = Processoren.objects
    return render_to_response('index.html', {'Processoren': processoren},
                              context_instance=RequestContext(request))



def processoren(request):

    # Get all posts from DB
    # Aantal per pagina en pagina nummer
    start, end = limits(request)

    processorenlijst = Processoren.objects.filter(categorie__contains='Processor')[start:end]
    #processoren = json.dumps(list(uniArray))
    return render_to_response('processoren.html', {'Processoren': processoren},
                              context_instance=RequestContext(request))

def behuizingen(request):

    # Get all posts from DB
    # Aantal per pagina en pagina nummer
    start, end = limits(request)

    processorenlijst = Processoren.objects(categorie__contains='Behuizing')[start:end]
    return render_to_response('behuizing.html', {'Processoren': processoren},
                              context_instance=RequestContext(request))

def geheugen(request):

    # Get all posts from DB
    # Aantal per pagina en pagina nummer
    start, end = limits(request)

    processorenlijst = Processoren.objects(categorie__contains='Geheugen')[start:end]
    return render_to_response('geheugen.html', {'Processoren': processoren},
                              context_instance=RequestContext(request))

def gpu(request):

    # Get all posts from DB
    # Aantal per pagina en pagina nummer
    start, end = limits(request)

    processorenlijst = Processoren.objects(categorie__contains='Grafische kaarten')[start:end]
    return render_to_response('gpu.html', {'Processoren': processoren},
                              context_instance=RequestContext(request))

def hardeschijf(request):

    # Get all posts from DB
    # Aantal per pagina en pagina nummer
    start, end = limits(request)

    processorenlijst = Processoren.objects(categorie__contains='Harde schijven')[start:end]
    return render_to_response('hardeschijf.html', {'Processoren': processoren},
                              context_instance=RequestContext(request))

def koeling(request):

    # Get all posts from DB
    # Aantal per pagina en pagina nummer
    start, end = limits(request)

    processorenlijst = Processoren.objects(categorie__contains='Koeling')[start:end]
    return render_to_response('koeling.html', {'Processoren': processoren},
                              context_instance=RequestContext(request))

def moederborden(request):

    # Get all posts from DB
    # Aantal per pagina en pagina nummer
    processorenlijst = Processoren.objects(categorie__contains='Moederborden').all()
    processoren = listing(request, processorenlijst, 15)
    return render_to_response('moederbord.html', {'Processoren': processoren},
                              context_instance=RequestContext(request))

def optischeschijf(request):

    # Get all posts from DB
    # Aantal per pagina en pagina nummer
    start, end = limits(request)

    processorenlijst = Processoren.objects(categorie__contains='DVD, Blu-ray & backup')[start:end]
    return render_to_response('optischeschijf.html', {'Processoren': processoren},
                              context_instance=RequestContext(request))

def voedingen(request):

    # Get all posts from DB
    # Aantal per pagina en pagina nummer
    start, end = limits(request)

    processorenlijst = Processoren.objects(categorie__contains='Voeding')[start:end]
    return render_to_response('voeding.html', {'Processoren': processoren},
                              context_instance=RequestContext(request))

def pages(request):
    aantal = request.GET.get('aantal', app)
    pagina = request.GET.get('pagina', '1')
    aantal = int(aantal)
    pagina = int(pagina) - 1
    return aantal, pagina

def limits(request):
    app, pagina = pages(request)
    start = app * pagina
    end = app * pagina + app
    return start, end

def listing(request, processorenlijst, aantal):
    paginator = Paginator(processorenlijst,15)
    pagina = request.GET.get('pagina')

    try:
        processoren = paginator.page(pagina)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        processoren = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        processoren = paginator.page(paginator.num_pages)

    return processoren
