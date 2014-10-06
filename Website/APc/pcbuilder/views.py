from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Processoren
import datetime

def index(request):
    if request.method == 'POST':
       # save new post
       titel = request.POST['title']
       prijs = request.POST['price']
       categorie = request.POST['price']
       image = request.POST['price']
       omschrijving = request.POST['price']

       processoren = Processoren(titel=titel)
       processoren.prijs = prijs
       processoren.categorie = categorie
       processoren.image = image
       processoren.omschrijving = omschrijving
       processoren.save()

    # Get all posts from DB
    processoren = Processoren.objects 
    return render_to_response('index.html', {'Processoren': processoren},
                              context_instance=RequestContext(request))

