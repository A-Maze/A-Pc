from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.shortcuts import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.template import loader
from django.http import HttpResponse
from bson.json_util import dumps
from pcbuilder.views import *
import time
from django.forms.util import ErrorList
from models import Processoren, Moederborden, Koeling, Behuizingen, Grafische, Harde, Dvd, Geheugen, Voeding, Views, Select, ViewsPerDatum, Login, Users, Registreer, SearchQuery

def registreer(request):
    #user = Users(Voornaam='', Achternaam='', Email='', Wachtwoord='', Rechten='0')
    #user.save()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        formregistreer = Registreer(request.POST)
        # check whether it's valid:
        if formregistreer.is_valid():
            voornaam = formregistreer.cleaned_data['voornaam']
            achternaam = formregistreer.cleaned_data['achternaam']
            email = formregistreer.cleaned_data['email']
            wachtwoord = formregistreer.cleaned_data['wachtwoord']
            try:
                selectedEerder=Users.objects.get(Email=email)
                formregistreer.errors[""] = ErrorList([u"Het opgegeven email adres is al geregistreerd!"])
            except Users.DoesNotExist:
                if(formregistreer.cleaned_data['wachtwoord'] == formregistreer.cleaned_data['Herhaal_wachtwoord']):
                    voeg_toe = Users(Voornaam=voornaam, Achternaam=achternaam, Email=email, Wachtwoord=wachtwoord, Rechten='0')
                    voeg_toe.save()
                    return HttpResponseRedirect('/login/')
                else:
                    formregistreer.errors[""] = ErrorList([u"De opgegeven wachtwoorden komen niet overeen!"])
    else:
        formregistreer = Registreer()
    return render_to_response('registreer.html',{'registreer': formregistreer},
                              context_instance=RequestContext(request))


def login(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Login(request.POST)
        # check whether it's valid:
        if form.is_valid():
            email = form.cleaned_data['email']
            wachtwoord = form.cleaned_data['wachtwoord']
            print(email)
            try:
                selectedEerder=Users.objects.get(Email=email, Wachtwoord=wachtwoord)
                request.session['email'] = email;
                request.session['Rechten'] = selectedEerder.Rechten
                return HttpResponseRedirect('/')
            except Users.DoesNotExist:
                selectedEerder = None
                form.errors[""] = ErrorList([u"Email of wachtwoord komen niet overeen!"])
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Login()

    return render_to_response('login.html',{'form': form},
                              context_instance=RequestContext(request))

def loguit(request):
    try:
        del request.session['email']
        del request.session['Rechten']
        return HttpResponseRedirect('/login/')
    except KeyError:
        return HttpResponseRedirect('/login/')

