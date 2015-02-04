from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.shortcuts import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.template import loader
from django.http import HttpResponse
from bson.json_util import dumps
from pcbuilder.compatibility import *
from pcbuilder.filters import *
from pcbuilder.compile import *
from pcbuilder.selection import *
from pcbuilder.dashboard import *
import json as simplejson
from models import Processoren, Moederborden, Koeling, Behuizingen, Grafische, Harde, Dvd, Geheugen, Voeding, Views, Select, ViewsPerDatum
from models import Processoren, Moederborden, Koeling, Behuizingen, Grafische, Harde, Dvd, Geheugen, Voeding, Views, Select, ViewsPerDatum, Login, Users, Registreer, SearchQuery, Bestellingen
from itertools import chain
from django.db.models import Max
import json, time, sys
from random import randint
from django.forms.util import ErrorList

data = [Processoren,Moederborden,Koeling,Behuizingen,Grafische,Harde,Dvd,Geheugen,Voeding]
dataFiltered = {}
for model in data:
    categorieNaam = model.__name__
    empty = unicode("")
    filteredModel = model.objects.filter((Q(prijs__exists=True) & Q(naam__exists=True) & Q(stock__exists=True)))
    dataFiltered[categorieNaam] = filteredModel
    
app = 15

def bestellingen(request):
    return render_to_response('bestellingen.html',{},
                             context_instance=RequestContext(request))

def bestel(request):
    categorieen = ['processoren', 'moederborden', 'grafische', 'harde', 'dvd', 'koeling', 'geheugen', 'voeding', 'behuizingen']
    naam = []
    naamlink = []

    j = 0
    for i in categorieen:
        if i in request.session:
            naam.insert(j, request.session[i+'id'])
            naamlink.insert(j, request.session[i+'link'])
        else:
            naam.insert(j, ' ')
            naamlink.insert(j, ' ')
        j = j+1

    if 'email' in request.session:
        email = request.session['email']
    else:
        return HttpResponseRedirect('/')

    try:
        old_bestelling=Bestellingen.objects.get(Email=email)
        old_bestelling.Processoren = naam[0]
        old_bestelling.Moederborden = naam[1]
        old_bestelling.Grafische = naam[2]
        old_bestelling.Harde = naam[3]
        old_bestelling.Dvd = naam[4]
        old_bestelling.Koeling = naam[5]
        old_bestelling.Geheugen = naam[6]
        old_bestelling.Voeding = naam[7]
        old_bestelling.Behuizingen = naam[8]
        old_bestelling.ProcessorenLink = naamlink[0]
        old_bestelling.MoederbordenLink = naamlink[1]
        old_bestelling.GrafischeLink = naamlink[2]
        old_bestelling.HardeLink = naamlink[3]
        old_bestelling.DvdLink = naamlink[4]
        old_bestelling.KoelingLink = naamlink[5]
        old_bestelling.GeheugenLink = naamlink[6]
        old_bestelling.VoedingLink = naamlink[7]
        old_bestelling.BehuizingenLink = naamlink[8]
        old_bestelling.save()
    except Bestellingen.DoesNotExist:
        new_bestelling=Bestellingen(Email=email, Processoren=naam[0], Moederborden=naam[1], Grafische=naam[2], Harde=naam[3],Dvd=naam[4],Koeling=naam[5],Geheugen=naam[6],Voeding=naam[7],Behuizingen=naam[8], ProcessorenLink=naamlink[0], MoederbordenLink=naamlink[1], GrafischeLink=naamlink[2], HardeLink=naamlink[3],DvdLink=naamlink[4],KoelingLink=naamlink[5],GeheugenLink=naamlink[6],VoedingLink=naamlink[7],BehuizingenLink=naamlink[8])
        new_bestelling.save()

    return HttpResponseRedirect('/bestellingen/')

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

def wijzigRechten(request):
    rechten = request.GET.get('rechten')
    email = request.GET.get('email')
    try:
        selectedEerder=Users.objects.get(Email=email)
        selectedEerder.Rechten = rechten
        selectedEerder.save()
        if(request.session['email'] == email):
            request.session['Rechten'] = rechten
    except Users.DoesNotExist:
        print("fout!")

    return HttpResponseRedirect('/dashboard/')

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



def index(request):
    # Get all posts from DB
    processoren = Processoren.objects

    #all the available prices
    prijzen = [request.session.get('processorenprijs'),
    request.session.get('moederbordenprijs'),
    request.session.get('grafischeprijs'),
    request.session.get('hardeprijs'),
    request.session.get('dvdprijs'),
    request.session.get('koelingprijs'),
    request.session.get('geheugenprijs'),
    request.session.get('voedingprijs'),
    request.session.get('behuizingenprijs')]

    links = [request.session.get('processorenlink'),
    request.session.get('moederbordenlink'),
    request.session.get('grafischelink'),
    request.session.get('hardelink'),
    request.session.get('dvdlink'),
    request.session.get('koelinglink'),
    request.session.get('geheugenlink'),
    request.session.get('voedinglink'),
    request.session.get('behuizingenlink')]

    totaalprijs = 0
    #loop through the prices
    for prijs in prijzen:
        if not prijs is None:
            totaalprijs += prijs

    filteredLinks = []

    for link in links:
        if not link is None:
            filteredLinks.append(link)

    jsonLinks = dumps(filteredLinks)

    return render_to_response('index.html',{'Totaalprijs': totaalprijs,'JSONLinks': jsonLinks},
                              context_instance=RequestContext(request))

def contact(request):
    processoren = Processoren.objects
    return render_to_response('contact.html',
                              context_instance=RequestContext(request))

def search(request):
    if request.method == "POST":
        query = request.POST.get('search')
        searchDatabase(query, request)
        #componentenArray = [Processoren, Moederborden, Koeling, Behuizingen, Grafische, Harde, Dvd, Geheugen, Voeding]

        print query

        filtert_Processoren = Processoren.objects.filter(naam__icontains=query)    
        filtert_Moederborden = Moederborden.objects.filter(naam__icontains=query)
        filtert_Koeling = Koeling.objects.filter(naam__icontains=query)
        filtert_Behuizingen = Behuizingen.objects.filter(naam__icontains=query)
        filtert_Grafische = Grafische.objects.filter(naam__icontains=query)
        filtert_Harde = Harde.objects.filter(naam__icontains=query)
        filtert_Dvd = Dvd.objects.filter(naam__icontains=query)
        filtert_Geheugen = Geheugen.objects.filter(naam__icontains=query)    
        filtert_Voeding = Voeding.objects.filter(naam__icontains=query) 

        # querysets = [filtert_Processoren,filtert_Moederborden,filtert_Koeling,filtert_Behuizingen,filtert_Grafische,filtert_Harde,filtert_Dvd,filtert_Geheugen,filtert_Voeding]

        filtert = filtert_Processoren 
        filtert = list(chain(filtert_Processoren,filtert_Moederborden,filtert_Koeling,filtert_Behuizingen,filtert_Grafische,filtert_Harde,filtert_Dvd,filtert_Geheugen,filtert_Voeding))
        
        
        print filtert
        filterComponents = listing(request, filtert, 15)

        bereik, diff, current_page = paginas(filtert, filterComponents)


        json = {}
        json['Componenten'] = render_to_string('search.html', {'Componenten': filterComponents , 'Range':bereik, 'Diff':diff, "page":current_page}, context_instance=RequestContext(request))
        json = dumps(json)
        return HttpResponse(json,content_type="application/json")

    else:
        return render_to_response('search.html', 
                                  context_instance=RequestContext(request))


def searchDatabase(query, request):
    gevonden = 0


    for search in SearchQuery.objects:
        print('aan het zoeken')
        if str(query) == str(search.Zoekwoord):
            aantal = int(search.Aantal)
            searchSet=SearchQuery.objects.get(Zoekwoord=query)
            nieuwAantal = aantal+1
            nieuwAantal = str(nieuwAantal)
            searchSet.Aantal = nieuwAantal
            searchSet.save()
            gevonden = 1
            #return HttpResponse(str(nieuwAantal))
        else:
            pass

    print('klaar met zoeken')
    if gevonden == 0:
        #zet views collectie de id als de id die is meegegeven het aantal op 15 (moet nog aan gewerkt worden)
        searchNieuw = SearchQuery(Zoekwoord=query, Aantal='1')
        #slaat de weergaven op in de db
        searchNieuw.save()
        #return HttpResponse('Niks gevonden')

    #je gaat weer terug naar de pagina



def mail(request):
    name = request.POST.get('name', '')
    subject = request.POST.get('type', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')






def renderToTemplate(request):
    #gets the request path without /
    requestPath = request.path[1:-1]
    print requestPath
    componentenLijst, merken = filters(request, dataFiltered[requestPath.title()])
    minPriceSliderValue, maxPriceSliderValue = getGrenzen(componentenLijst)
    componenten = listing(request, componentenLijst, 15)        
    bereik, diff, current_page = paginas(componentenLijst, componenten)

    htmlStr = requestPath + ".html"

    if request.method == 'POST':
        json = {}
        json['Componenten'] = render_to_string(htmlStr, {'Componenten': componenten, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page, "merken": merken }, context_instance=RequestContext(request))
        json = dumps(json)
        return HttpResponse(json,content_type="application/json")
    else:
        return render_to_response(htmlStr, {'Componenten': componenten, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page, "merken": merken },
                              context_instance=RequestContext(request))




def listing(request, componentenlijst, aantal):
    paginator = Paginator(componentenlijst,15)
    try:
        pagina = request.POST['pageNumber']
    except:
        pagina = 1

    try:
        componenten = paginator.page(pagina)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        componenten = paginator.page(1)
    except EmptyPage:
        # If page is out of bereik (e.g. 9999), deliver last page of results.
        componenten = paginator.page(paginator.num_pages)

    return componenten

def paginas(componentenlijst, componenten):
    bereik = [-3, -2, -1, 0, 1, 2, 3]
    pages = Paginator(componentenlijst, 15).page_range
    current_page = componenten.number

    # Difference between current page
    # Fill with 0 because pages start at 1
    diff = [0]
    for p in pages:
        diff.append(int(p - current_page))

    return bereik, diff, current_page

def compile(request):
    buildpc(request);
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

