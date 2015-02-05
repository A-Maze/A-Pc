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
from models import Processoren, Moederborden, Koeling, Behuizingen, Grafische, Harde, Dvd, Geheugen, Voeding, Views, Select, ViewsPerDatum, Login, Users, Registreer, SearchQuery



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
        return HttpResponseRedirect('/dashboard/')


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
                    nieuwAantal = aantal+1.0
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
            weergaven = Views(Id=productid, Categorie=categorie, Aantal='1.0')
            #slaat de weergaven op in de db
            weergaven.save()
        #return HttpResponse('Niks gevonden')

    #je gaat weer terug naar de pagina
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def ViewsPerDag(action, request):
    ObjectenLijst = ViewsPerDatum.objects
    LaatsteObject = len(ObjectenLijst) - 1
    if(LaatsteObject >= 0):
        lastone = ObjectenLijst[LaatsteObject].Datum
    else:
        lastone = "01/01/2014"
    datum = time.strftime("%d/%m/%Y")
    datumString = ""+lastone+""
    datumArray = []
    datumArray.extend(datumString.split("/"))
    datumLater = str(int(datumArray[0])+1).zfill(2)+"/"+str(datumArray[1]).zfill(2)+"/"+str(datumArray[2])
    datumsLater = []
    done = False
    maand = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    gevonden = 0


    for viewsperdatum in ViewsPerDatum.objects:
            if str(datum) == str(viewsperdatum.Datum):
                if action == 'add':
                    aantal = float(viewsperdatum.Aantal)
                    selected=ViewsPerDatum.objects.get(Datum=datum)
                    nieuwAantal = aantal+1.0
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
            i=0
            while(datumLater != datum):
                if((str(int(datumArray[0])+1).zfill(2)+"/"+str(datumArray[1]).zfill(2)+"/"+str(datumArray[2])) != datum):
                    if(int(datumArray[0])+1 <= maand[int(datumArray[1])]):
                        datumLater = str(int(datumArray[0])+1).zfill(2)+"/"+str(datumArray[1]).zfill(2)+"/"+str(datumArray[2])
                        datumArray[0] = str(int(datumArray[0])+1)
                        datumArray[1] = str(datumArray[1])
                        datumArray[2] = str(datumArray[2])
                    elif(int(datumArray[0])+1 > maand[int(datumArray[1])]):
                        if(int(datumArray[1])+1 <= 12):
                            datumLater = "01/"+str(int(datumArray[1])+1).zfill(2)+"/"+str(datumArray[2])
                            datumArray[0] = 01
                            datumArray[1] = str(int(datumArray[1])+1)
                            datumArray[2] = str(datumArray[2])
                        elif(int(datumArray[1])+1 > 12):
                            datumLater = str().zfill(2)+"/"+str(1).zfill(2)+"/"+str(int(datumArray[2])+1)
                            datumArray[0] = 01
                            datumArray[1] = 01
                            datumArray[2] = str(int(datumArray[2])+1)
                    datumsLater.insert(i, datumLater)
                    i = i + 1
                else:
                    done = True
                    break

            for i in datumsLater:
                datumLeeg = ViewsPerDatum(Datum=i, Aantal='0.0')
                datumLeeg.save()

            datumVandaag = ViewsPerDatum(Aantal='1.0', Datum=datum)
            #slaat de geselecteerden op in de db
            datumVandaag.save()
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
