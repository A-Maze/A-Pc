from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.shortcuts import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.template import loader
from django.http import HttpResponse
from bson.json_util import dumps
from pcbuilder.views import *
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