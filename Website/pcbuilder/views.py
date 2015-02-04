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
import json as simplejson
from models import Processoren, Moederborden, Koeling, Behuizingen, Grafische, Harde, Dvd, Geheugen, Voeding, Views, Select, ViewsPerDatum
from models import Processoren, Moederborden, Koeling, Behuizingen, Grafische, Harde, Dvd, Geheugen, Voeding, Views, Select, ViewsPerDatum, Login, Users, Registreer, SearchQuery
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

def loguit(request):
    try:
        del request.session['email']
        del request.session['Rechten']
        return HttpResponseRedirect('/login/')
    except KeyError:
        return HttpResponseRedirect('/login/')


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

        #filtert = list(chain(filtert_Processoren))
        filtert = filtert_Processoren 
        print "combining...."
        filtert = list(chain(filtert_Processoren))
        
        
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

def select(request):
    #getting all the variables from the url
    product = request.GET.get('product')
    categorie = request.GET.get('categorie')
    prijs = request.GET.get('prijs')
    productid = request.GET.get('productid')
    herkomst = request.GET.get('herkomst')
    link = request.GET.get('link')
    prijs = float(prijs)

    #Viewers(productid, categorie, 'delete', request)
    #Selected(productid, categorie, 'add', request)
    #ViewsPerDag('delete', request)


    categorie.replace(" ", "")
    categorie.replace(",", "")
    request.session[categorie] = True
    productstring = categorie + "naam"
    categorieprijs = categorie + "prijs"
    categorieid = categorie + "id"
    print categorieid
    categorieherkomst = categorie + "herkomst"
    categorielink = categorie + "link"

    #setting the session variables for the category
    request.session[productstring] = product
    request.session[categorieprijs] = prijs
    request.session[categorieid] = productid
    request.session[categorieherkomst] = herkomst
    request.session[categorielink] = link

    return HttpResponseRedirect(request.META.get('/','/'))

def deselect(request):
    product = request.GET.get('product')
    categorie = request.GET.get('categorie')
    prijs = request.GET.get('prijs')
    categorie.replace(" ", "")
    productid = request.GET.get('productid')
    
    #Viewers(productid, categorie, 'delete', request)
    #ViewsPerDag('delete', request)

    del request.session[categorie]
    productid = categorie + "id"
    productstring = categorie + "naam"
    productprijs = categorie + "prijs"
    productlink = categorie + "link"
    print type(product)
    print type(request.session[productstring])
    print product
    print request.session[productstring]
    if request.session[productstring] == product:
        print "deselect called"
        del request.session[productid]
        del request.session[productstring]
        del request.session[productprijs]
        del request.session[productlink]
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    


def detail(request):
    categorie = request.GET.get('categorie')
    productid = request.GET.get('productid')

    try:
        currentID = request.session[categorie + "id"]
        currentherkomst = request.session[categorie + "herkomst"]
        existing = True
    except KeyError:
        existing = False
    
    if (categorie == "processoren"):
        categorieObject = Processoren
    elif (categorie == "moederborden"):
        categorieObject = Moederborden
    elif (categorie == "koeling"):
        categorieObject = Koeling
    elif (categorie == "grafische"):
        categorieObject = Grafische
    elif (categorie == "harde"):
        categorieObject = Harde
    elif (categorie == "dvd"):
        categorieObject = Dvd
    elif (categorie == "koeling"):
        categorieObject = Koeling
    elif (categorie == "geheugen"):
        categorieObject = Geheugen
    elif (categorie == "voeding"):
        categorieObject = Voeding
    elif (categorie == "behuizingen"):
        categorieObject = Behuizingen

    #Viewers(productid, categorie, 'add', request)
    #ViewsPerDag('add', request)

    component = categorieObject.objects.get(id=productid)



    if(component.herkomst):
        ziplist = zip(component.herkomst, component.stock, component.link, component.prijs)


    #if currentproduct and currentherkomst exist render them to response as well
    if existing:
        return render_to_response('detail.html', {'component': component, 'Productid': productid, 'Ziplist': ziplist, 'CurrentID': currentID, 'Currentherkomst': currentherkomst })
    else:
        return render_to_response('detail.html', {'component': component, 'Productid': productid, 'Ziplist': ziplist})

def Viewers(productid, categorie, action, request):
    #haalt de id uit de link
    #productid = request.GET.get('productid')
    gevonden = 0
    datum = time.strftime("%d/%m/%Y")


    for views in Views.objects:
            if str(productid) == str(views.Id):
                if action == 'add':
                    aantal = float(views.Aantal)
                    viewss=Views.objects.get(Id=productid)
                    nieuwAantal = aantal+0.5
                    nieuwAantal = str(nieuwAantal)
                    viewss.Aantal = nieuwAantal
                    viewss.save()
                    gevonden = 1
                    #return HttpResponse(str(nieuwAantal))
                elif action == 'delete':
                    aantal = float(views.Aantal)
                    viewss=Views.objects.get(Id=productid)
                    nieuwAantal = aantal-1.0
                    nieuwAantal = str(nieuwAantal)
                    viewss.Aantal = nieuwAantal
                    viewss.save()
                    gevonden = 1
                    #return HttpResponse(str(nieuwAantal))
            else:
                pass
    if gevonden == 0:
        if(action == 'add'):
            #zet views collectie de id als de id die is meegegeven het aantal op 15 (moet nog aan gewerkt worden)
            weergaven = Views(Id=productid, Categorie=categorie, Aantal='0.5')
            #slaat de weergaven op in de db
            weergaven.save()
        #return HttpResponse('Niks gevonden')

    #je gaat weer terug naar de pagina
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def ViewsPerDag(action, request):
    datum = time.strftime("%d/%m/%Y")
    gevonden = 0
    maand = [0,31,28,31,30,31,30,31,31,30,31,30,31]

    datumString = ""+datum+""
    datumArray = []
    datumArray.extend(datumString.split("/"))
    dagEerder = int(datumArray[0])-1
    maandEerder = int(datumArray[1])
    jaarEerder = int(datumArray[2])
    jaarEerderString = str(jaarEerder)
    maandEerderString = str(maandEerder)
    if(maandEerder < 10):
        maandEerderString = "0"+maandEerderString
    dagLater = dagEerder
    maandLater = maandEerder
    jaarLater = jaarEerder
    jaarLaterString = str(jaarLater)
    maandLaterString = str(maandLater)
    if(maandLater < 10):
        maandLaterString = "0"+maandLaterString
    selectedDate = None
    
    if(dagEerder >= 10):
        dagEerderString = str(dagEerder)
    elif(dagEerder < 10):
        dagEerderString = "0"+str(dagEerder)
    datumEerder = dagEerderString+"/"+datumArray[1]+"/"+datumArray[2]
    print(datumArray)


    for viewsperdatum in ViewsPerDatum.objects:
            if str(datum) == str(viewsperdatum.Datum):
                if action == 'add':
                    aantal = float(viewsperdatum.Aantal)
                    selected=ViewsPerDatum.objects.get(Datum=datum)
                    nieuwAantal = aantal+0.5
                    nieuwAantal = str(nieuwAantal)
                    selected.Aantal = nieuwAantal
                    selected.save()
                    gevonden = 1
                    #return HttpResponse(str(nieuwAantal))
                elif action == 'delete':
                    aantal = float(viewsperdatum.Aantal)
                    selected=ViewsPerDatum.objects.get(Datum=datum)
                    nieuwAantal = aantal-1.0
                    nieuwAantal = str(nieuwAantal)
                    selected.Aantal = nieuwAantal
                    selected.save()
                    gevonden = 1
                    #return HttpResponse(str(nieuwAantal))
            else:
                pass
    if gevonden == 0:
        if(action == 'add'):
            #zet selected collectie de id als de id die is meegegeven het aantal op 15 (moet nog aan gewerkt worden)
            



            try:
                selectedEerder=ViewsPerDatum.objects.get(Datum=datumEerder)
            except ViewsPerDatum.DoesNotExist:
                selectedEerder = None
            if(selectedEerder == None):
                print("staat niet in db")
                selectedDate = datumEerder
                while(selectedEerder == None):
                    print("in de loop")
                    if(int(dagEerder-1) > 0):
                        dagEerder = dagEerder-1
                        if(dagEerder >= 10):
                            dagEerderString = str(dagEerder)
                        elif(dagEerder < 10):
                            dagEerderString = str(dagEerder)
                            dagEerderString = "0"+dagEerderString
                        else:
                            break
                    elif(int(dagEerder-1) <= 0):
                        if(int(maandEerder-1) > 0):
                            maandEerder = maandEerder-1
                            dagEerder = maand[maandEerder]
                            dagEerderString = str(dagEerder)
                            if(maandEerder < 10):
                                maandEerderString = str(maandEerder)
                                maandEerderString = "0"+maandEerderString
                            elif(maandEerder >= 10):
                                maandEerderString = str(maandEerder)
                        elif(int(maandEerder-1) <= 0):
                            jaarEerder = jaarEerder-1
                            maandEerder = 12
                            dagEerder = maand[maandEerder]
                            dagEerderString = str(dagEerder)
                            maandEerderString = str(maandEerder)
                            jaarEerderString = str(jaarEerder)
                    else:
                        selectedEerder = "selectedDate"
                        print("infinite loop")
                        break
                    datumEerder = dagEerderString+"/"+maandEerderString+"/"+jaarEerderString

                    if(datumEerder == "01/12/2014"):
                        selectedDate = datumEerder
                        datumLater = datumEerder
                        dagLater = dagEerder
                        maandLater = maandEerder
                        jaarLater = jaarEerder
                        datumLater = datumEerder
                        print("Datum Eerder:"+str(dagLater)+"+"+str(maandLater)+"+"+str(jaarLater))
                        break

                    print(datumEerder)
                    try:
                        selectedEerder=ViewsPerDatum.objects.get(Datum=datumEerder)
                        selectedDate = datumEerder
                        datumLater = datumEerder
                        dagLater = dagEerder
                        maandLater = maandEerder
                        jaarLater = jaarEerder
                        datumLater = datumEerder
                    except ViewsPerDatum.DoesNotExist:
                        selectedEerder = None
            elif(selectedEerder != None):
                print("staat al in db")
            

            if(selectedDate != None):
                try:
                    datumLater = dagLater + 1
                    datumLater = str(datumLater)+"/"+str(maandEerder)+"/"+str(jaarEerder)
                    print(datumLater)
                    selectedLater=ViewsPerDatum.objects.get(Datum=datumLater)
                except ViewsPerDatum.DoesNotExist:
                    selectedLater = None
                if(selectedLater == None):
                    print("aangevuld")
                    while(selectedLater == None):
                        print(datumLater)
                        print(dagLater)
                        print(maandLater)
                        print(jaarLater)
                        dagLater = dagLater+1
                        if((dagLater <= maand[maandLater])):
                            print("if dag later kleiner is als het aantal dagen")
                            if(dagLater < 10):
                                dagLaterString = str(dagLater)
                                dagLaterString = "0"+dagLaterString
                            else:
                                dagLaterString = str(dagLater)
                            if(maandLater < 10):
                                maandLaterString = str(maandLater)
                                maandLaterString = "0"+maandLaterString
                            elif(maandLater >= 10):
                                maandLaterString = str(maandLater)
                            jaarLaterString = str(jaarLater)
                        elif((maandLater < 12) and (dagLater > maand[maandLater])):
                            print("if dag later groter is als het aantal dagen en de maand later kleiner als 12")
                            maandLater = maandLater + 1
                            if(maandLater < 10):
                                maandLaterString = str(maandLater)
                                maandLaterString = "0"+maandLaterString
                            elif(maandLater >= 10):
                                maandLaterString = str(maandLater)
                            dagLater = 01
                            dagLaterString = str(dagLater)
                            jaarLaterString = str(jaarLater)
                        elif((maandLater >= 12) and (dagLater > maand[maandLater])):
                            print("if dag later groter is als het aantal dagen en de maand later groter als 12")
                            maandLater = 01
                            maandLaterString = str(maandLater)
                            maandLaterString = "0"+maandLaterString
                            dagLater = 01
                            dagLaterString = str(dagLater)
                            dagLaterString = "0"+dagLaterString
                            jaarLater = jaarLater + 1
                            jaarLaterString = str(jaarLater)
                            
                        print(dagLaterString+maandLaterString+jaarLaterString)
                        datumLater = dagLaterString+"/"+maandLaterString+"/"+jaarLaterString
                        print(datumLater)
                        if(datumLater == datum):
                            print("datum later gelijk aan datum:"+datumLater)
                            break
                        print("datum later:"+datumLater)
                        try:
                            print(datumLater)
                            selectedLater=ViewsPerDatum.objects.get(Datum=datumLater)
                            print("komt hier bij")
                        except ViewsPerDatum.DoesNotExist:
                            selectedLater = None
                        if(selectedLater == None and datumLater != datum):
                            print("komt hier bij")
                            geselecteerdLater = ViewsPerDatum(Aantal='0.0', Datum=datumLater)
                            geselecteerdLater.save()
                            #Voor random nummer: str(randint(0,100))
                else:
                    print("nog niet aangevuld")


            elif(selectedDate == None):
                print("Al toegevoegd")




            geselecteerd = ViewsPerDatum(Aantal='0.5', Datum=datum)
            #slaat de geselecteerden op in de db
            geselecteerd.save()
        #return HttpResponse('Niks gevonden')

    #je gaat weer terug naar de pagina
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def Selected(productid, categorie, action, request):
    #haalt de id uit de link
    #productid = request.GET.get('productid')
    gevonden = 0


    for select in Select.objects:
            if str(productid) == str(select.Id):
                if action == 'add':
                    aantal = float(select.Aantal)
                    selected=Select.objects.get(Id=productid)
                    nieuwAantal = aantal+1.0
                    nieuwAantal = str(nieuwAantal)
                    selected.Aantal = nieuwAantal
                    selected.save()
                    gevonden = 1
                    #return HttpResponse(str(nieuwAantal))
                elif action == 'delete':
                    aantal = float(select.Aantal)
                    selected=Select.objects.get(Id=productid)
                    nieuwAantal = aantal-1.0
                    nieuwAantal = str(nieuwAantal)
                    selected.Aantal = nieuwAantal
                    selected.save()
                    gevonden = 1
                    #return HttpResponse(str(nieuwAantal))
            else:
                pass
    if gevonden == 0:
        if(action == 'add'):
            #zet selected collectie de id als de id die is meegegeven het aantal op 15 (moet nog aan gewerkt worden)
            geselecteerd = Select(Id=productid, Categorie=categorie, Aantal='0.5')
            #slaat de geselecteerden op in de db
            geselecteerd.save()
        #return HttpResponse('Niks gevonden')

    #je gaat weer terug naar de pagina
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))




def dashboard(request):
    dashboardlijst = Views.objects.order_by('-Aantal')
    dashboardlijst = listing(request, dashboardlijst, 10)
    searchQueryLijst2 = SearchQuery.objects.order_by('-Aantal', 'Zoekwoord')
    userlijst = Users.objects.order_by('Email')

    mylist = []
    userlist = []
    rechtenlist = []
    searchQueryLijst = []
    searchQueryLijst1 = []
    viewsperdag = []
    datumsperdag = []
    processorenperc = 0;
    moederbordenperc = 0;
    grafischeperc = 0;
    behuizingenperc = 0;
    hardeperc = 0;
    dvdperc = 0;
    koelingperc = 0;
    geheugenperc = 0;
    voedingperc = 0;
    i = 0
    for viewss in dashboardlijst:
        mylist.insert(i, viewss.Id)
        i = i +1
    j = 0
    for users in userlijst:
        userlist.insert(j, users.Email)
        rechtenlist.insert(j, users.Rechten)
        j = j +1
    k = 0
    for search in searchQueryLijst2:
        searchQueryLijst.insert(k, search.Zoekwoord)
        searchQueryLijst1.insert(k, search.Aantal)
        k = k + 1
    for percentage in Views.objects:
        if percentage.Categorie == 'processoren':
            processorenperc = processorenperc + int(float(percentage.Aantal));
        elif percentage.Categorie == 'moederborden':
            moederbordenperc = moederbordenperc + int(float(percentage.Aantal));
        elif percentage.Categorie == 'voeding':
            voedingperc = voedingperc + int(float(percentage.Aantal));
        elif percentage.Categorie == 'geheugen':
            geheugenperc = geheugenperc + int(float(percentage.Aantal));
        elif percentage.Categorie == 'koeling':
            koelingperc = koelingperc + int(float(percentage.Aantal));
        elif percentage.Categorie == 'grafische':
            grafischeperc = grafischeperc + int(float(percentage.Aantal));
        elif percentage.Categorie == 'behuizingen':
            behuizingenperc = behuizingenperc + int(float(percentage.Aantal));
        elif percentage.Categorie == 'harde':
            hardeperc = hardeperc + int(float(percentage.Aantal));
        elif percentage.Categorie == 'dvd':
            dvdperc = dvdperc + int(float(percentage.Aantal));
        else:
            pass
    #totaalpercentage = processorenperc+moederbordenperc+grafischeperc+behuizingenperc+hardeperc+dvdperc+koelingperc+geheugenperc+voedingperc
    #processorenperc = (processorenperc/totaalpercentage)*100
    #moederbordenperc = (moederbordenperc/totaalpercentage)*100
    processorenlijst = []
    processorenlijst.extend(Processoren.objects.filter(id__in=mylist))
    processorenlijst.extend(Moederborden.objects.filter(id__in=mylist))
    processorenlijst.extend(Behuizingen.objects.filter(id__in=mylist))
    processorenlijst.extend(Grafische.objects.filter(id__in=mylist))
    processorenlijst.extend(Harde.objects.filter(id__in=mylist))
    processorenlijst.extend(Dvd.objects.filter(id__in=mylist))
    processorenlijst.extend(Koeling.objects.filter(id__in=mylist))
    processorenlijst.extend(Geheugen.objects.filter(id__in=mylist))
    processorenlijst.extend(Voeding.objects.filter(id__in=mylist))
    views = listing(request, processorenlijst, 10)

    viewsperdatumlijst = ViewsPerDatum.objects
    j = 0;
    for viewsdatums in viewsperdatumlijst:
        viewsperdag.insert(j, int(float(viewsdatums.Aantal)))
        j = j+1




    return render_to_response('dashboard.html', {'Componenten': views, 'Processorenpercentage': processorenperc,'Moederbordenpercentage': moederbordenperc,'Voedingpercentage': voedingperc,'Geheugenpercentage': geheugenperc,'Koelingpercentage': koelingperc,'Grafischepercentage':grafischeperc, 'Behuizingenpercentage':behuizingenperc, 'Dvdpercentage': dvdperc, 'Hardepercentage': hardeperc, 'ViewsPerDatum2': viewsperdag, 'Search': searchQueryLijst2, 'Userlist': userlijst},
                              context_instance=RequestContext(request))

def processoren(request):

    '''

db.processoren.find().forEach( function(processoren) {
    for(var i in processoren.prijs){
        processoren.prijs[i] = parseFloat(processoren.prijs[i]);
    }
    db.processoren.save(processoren);
});
    '''

    processorenlijst = Processoren.objects.filter(prijs__exists=True)
    processorenlijst, merken = filters(request, processorenlijst)
    minPriceSliderValue, maxPriceSliderValue = getGrenzen(processorenlijst)
    processoren = listing(request, processorenlijst, 15)
    bereik, diff, current_page = paginas(processorenlijst, processoren)


    if request.method == 'POST':
        json = {}
        json['Componenten'] = render_to_string('processoren.html', {'Componenten': processoren, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page, "merken": merken }, context_instance=RequestContext(request))
        json = dumps(json)
        return HttpResponse(json,content_type="application/json")
    else:
        return render_to_response('processoren.html', {'Componenten': processoren, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page, "merken": merken },
                              context_instance=RequestContext(request))

def behuizingen(request):
    behuizingenlijst, merken = filters(request, dataFiltered[sys._getframe().f_code.co_name.title()])
    minPriceSliderValue, maxPriceSliderValue = getGrenzen(behuizingenlijst)
    behuizingen = listing(request, behuizingenlijst, 15)        
    bereik, diff, current_page = paginas(behuizingenlijst, behuizingen)

    if request.method == 'POST':
        json = {}
        json['Componenten'] = render_to_string('behuizing.html', {'Componenten': behuizingen, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page, "merken": merken }, context_instance=RequestContext(request))
        json = dumps(json)
        return HttpResponse(json,content_type="application/json")
    else:
        return render_to_response('behuizing.html', {'Componenten': behuizingen, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page, "merken": merken },
                              context_instance=RequestContext(request))

def geheugen(request):
    geheugenlijst, merken = filters(request, dataFiltered[sys._getframe().f_code.co_name.title()])
    minPriceSliderValue, maxPriceSliderValue = getGrenzen(geheugenlijst)
    geheugen = listing(request, geheugenlijst, 15)        
    bereik, diff, current_page = paginas(geheugenlijst, geheugen)

    if request.method == 'POST':
        json = {}
        json['Componenten'] = render_to_string('geheugen.html', {'Componenten': geheugen, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page, "merken": merken }, context_instance=RequestContext(request))
        json = dumps(json)
        return HttpResponse(json,content_type="application/json")
    else:
        return render_to_response('geheugen.html', {'Componenten': geheugen, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page, "merken": merken },
                              context_instance=RequestContext(request))
def grafische(request):

    gpulijst, merken = filters(request, dataFiltered[sys._getframe().f_code.co_name.title()])
    minPriceSliderValue, maxPriceSliderValue = getGrenzen(gpulijst)
    gpu = listing(request, gpulijst, 15)        
    bereik, diff, current_page = paginas(gpulijst, gpu)

    if request.method == 'POST':
        json = {}
        json['Componenten'] = render_to_string('gpu.html', {'Componenten': gpu, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page, "merken": merken }, context_instance=RequestContext(request))
        json = dumps(json)
        return HttpResponse(json,content_type="application/json")
    else:
        return render_to_response('gpu.html', {'Componenten': gpu, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page, "merken": merken },
                              context_instance=RequestContext(request))
def harde(request):

    hardelijst, merken = filters(request, dataFiltered[sys._getframe().f_code.co_name.title()])
    minPriceSliderValue, maxPriceSliderValue = getGrenzen(hardelijst)
    harde = listing(request, hardelijst, 15)        
    bereik, diff, current_page = paginas(hardelijst, harde)

    if request.method == 'POST':
        json = {}
        json['Componenten'] = render_to_string('hardeschijf.html', {'Componenten': harde, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page, "merken": merken }, context_instance=RequestContext(request))
        json = dumps(json)
        return HttpResponse(json,content_type="application/json")
    else:
        return render_to_response('hardeschijf.html', {'Componenten': harde, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page, "merken": merken },
                              context_instance=RequestContext(request))

def koeling(request):

    koelinglijst, merken = filters(request, dataFiltered[sys._getframe().f_code.co_name.title()])
    minPriceSliderValue, maxPriceSliderValue = getGrenzen(koelinglijst)
    koelingen = listing(request, koelinglijst, 15)        
    bereik, diff, current_page = paginas(koelinglijst, koelingen)

    if request.method == 'POST':
        json = {}
        json['Componenten'] = render_to_string('koeling.html', {'Componenten': koelingen, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page, "merken": merken }, context_instance=RequestContext(request))
        json = dumps(json)
        return HttpResponse(json,content_type="application/json")
    else:
        return render_to_response('koeling.html', {'Componenten': koelingen, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page, "merken": merken },
                              context_instance=RequestContext(request))

def moederborden(request):

    moederbordenlijst, merken = filters(request, dataFiltered[sys._getframe().f_code.co_name.title()])
    print type(moederbordenlijst)
    minPriceSliderValue, maxPriceSliderValue = getGrenzen(moederbordenlijst)
    moederborden = listing(request, moederbordenlijst, 15)        
    bereik, diff, current_page = paginas(moederbordenlijst, moederborden)

    if request.method == 'POST':
        json = {}
        json['Componenten'] = render_to_string('moederbord.html', {'Componenten': moederborden, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page, "merken": merken }, context_instance=RequestContext(request))
        json = dumps(json)
        return HttpResponse(json,content_type="application/json")
    else:
        return render_to_response('moederbord.html', {'Componenten': moederborden, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page, "merken": merken },
                              context_instance=RequestContext(request))

def dvd(request):
    optischeschijflijst, merken = filters(request, dataFiltered[sys._getframe().f_code.co_name.title()])
    minPriceSliderValue, maxPriceSliderValue = getGrenzen(optischeschijflijst)
    optischeschijven = listing(request, optischeschijflijst, 15)        
    bereik, diff, current_page = paginas(optischeschijflijst, optischeschijven)

    if request.method == 'POST':
        json = {}
        json['Componenten'] = render_to_string('optischeschijf.html', {'Componenten': optischeschijven, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page, "merken": merken }, context_instance=RequestContext(request))
        json = dumps(json)
        return HttpResponse(json,content_type="application/json")
    else:
        return render_to_response('optischeschijf.html', {'Componenten': optischeschijven, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page, "merken": merken },
                              context_instance=RequestContext(request))



def voeding(request):

    voedinglijst, merken = filters(request, dataFiltered[sys._getframe().f_code.co_name.title()])
    minPriceSliderValue, maxPriceSliderValue = getGrenzen(voedinglijst)
    voedingen = listing(request, voedinglijst, 15)        
    bereik, diff, current_page = paginas(voedinglijst, voedingen)

    if request.method == 'POST':
        json = {}
        json['Componenten'] = render_to_string('voeding.html', {'Componenten': voedingen, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page, "merken": merken }, context_instance=RequestContext(request))
        json = dumps(json)
        return HttpResponse(json,content_type="application/json")
    else:
        return render_to_response('voeding.html', {'Componenten': voedingen, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page, "merken": merken },
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

