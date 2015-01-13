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
from pcbuilder.builds import *
import json as simplejson
from models import Processoren, Moederborden, Koeling, Behuizingen, Grafische, Harde, Dvd, Geheugen, Voeding
from itertools import chain
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
            totaalprijs += float(prijs.replace(",","."))

    filteredLinks = []

    for link in links:
        if not link is None:
            filteredLinks.append(link)

    filteredLinks = dumps(filteredLinks)

    return render_to_response('index.html',{'Totaalprijs': totaalprijs,'Links': filteredLinks},
                              context_instance=RequestContext(request))

def contact(request):
    processoren = Processoren.objects
    return render_to_response('contact.html',
                              context_instance=RequestContext(request))

def search(request):
    if request.method == "POST":
        query = request.POST.get('search')
        #componentenArray = [Processoren, Moederborden, Koeling, Behuizingen, Grafische, Harde, Dvd, Geheugen, Voeding]

        print "HOII"


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
        print "combining...."
        filtert = list(chain(filtert_Processoren))
        
        
        print filtert
        filterComponents = listing(request, filtert, 15)

        bereik, diff, current_page = paginas(filtert, filterComponents)

        json = {}
        json['filterComponents'] = render_to_string('search.html', {'filterComponents': filterComponents , 'Range':bereik, 'Diff':diff, "page":current_page}, context_instance=RequestContext(request))
        json = dumps(json)
        return HttpResponse(json,content_type="application/json")

    else:
        print ("1,2,3")
        return render_to_response('search.html', 
                                  context_instance=RequestContext(request))



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


    categorie.replace(" ", "")
    categorie.replace(",", "")
    prijs.replace(" ","")
    request.session[categorie] = True
    productstring = categorie + "naam"
    categorieprijs = categorie + "prijs"
    categorieid = categorie + "id"
    categorieherkomst = categorie + "herkomst"
    categorielink = categorie + "link"

    #setting the session variables for the category
    request.session[productstring] = product
    request.session[categorieprijs] = prijs
    request.session[categorieid] = productid
    request.session[categorieherkomst] = herkomst
    request.session[categorielink] = link

    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def deselect(request):
    product = request.GET.get('product')
    categorie = request.GET.get('categorie')
    prijs = request.GET.get('prijs')
    categorie.replace(" ", "")
    del request.session[categorie]
    productstring = categorie + "naam"
    productprijs = categorie + "prijs"
    if request.session[productstring] == product:
        del request.session[productstring]
        del request.session[productprijs]
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    


def detail(request):
    product = request.GET.get('product')
    categorie = request.GET.get('categorie')
    categorie = categorie.lower()
    prijs = request.GET.get('prijs')
    productid = request.GET.get('productid')
    #tries if currentproduct and currentherkomst actually exist and puts that in a variable
    try:
        currentproduct = request.session[categorie + "naam"]
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

    #makes a list of price,stock,link and herkomst
    for component in categorieObject.objects:
            if str(productid) == str(component.id):
                ziplist = zip(component.herkomst, component.stock, component.link, component.prijs)

    #if currentproduct and currentherkomst exist render them to response as well
    if existing:
        return render_to_response('detail.html', {'Componenten': (categorieObject.objects,), 'Categorie' : categorie.lower(), 'Product': product, 'Prijs': prijs, 'Productid': productid, 'Ziplist': ziplist, 'Currentproduct': currentproduct, 'Currentherkomst': currentherkomst },
        context_instance=RequestContext(request))
    else:
        return render_to_response('detail.html', {'Componenten': (categorieObject.objects,), 'Categorie' : categorie.lower(), 'Product': product, 'Prijs': prijs, 'Productid': productid, 'Ziplist': ziplist},
        context_instance=RequestContext(request))


def processoren(request):

    # Get all posts from DB
    # Aantal per pagina en pagina nummer
    minPriceSliderValue = 1500.1
    maxPriceSliderValue = 0.1

    processorenlijst = Processoren.objects

    #overgebleven componentenlijst afhankelijk van stock
    #Dit dient later afhaneklijk te worden van alle filters
    processorenlijst = filters(request, processorenlijst)

    for processoren in processorenlijst:

        if processoren.prijs:
            diestringnaam = processoren.prijs[0].replace(",",("."))
            if float(diestringnaam) < float(minPriceSliderValue):
                minPriceSliderValue = diestringnaam
            elif float(diestringnaam) > float(maxPriceSliderValue):
                maxPriceSliderValue = diestringnaam

    processoren = listing(request, processorenlijst, 15)
    
    bereik, diff, current_page = paginas(processorenlijst, processoren)


    if request.method == 'POST':
        json = {}
        json['Componenten'] = render_to_string('processoren.html', {'Componenten': processoren, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page }, context_instance=RequestContext(request))
        json = dumps(json)
        return HttpResponse(json,content_type="application/json")
    else:
        return render_to_response('processoren.html', {'Componenten': processoren, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page },
                              context_instance=RequestContext(request))

def behuizingen(request):

    # Get all posts from DB
    # Aantal per pagina en pagina nummer    
    minPriceSliderValue = 1500.1
    maxPriceSliderValue = 0.1

    behuizingenlijst = Behuizingen.objects

    #overgebleven componentenlijst afhankelijk van stock
    #Dit dient later afhaneklijk te worden van alle filters
    behuizingenlijst = filters(request,behuizingenlijst)
    behuizingen = listing(request, behuizingenlijst, 15)
    
    bereik, diff, current_page = paginas(behuizingenlijst, behuizingen)

    if request.method == 'POST':
        json = {}
        json['Componenten'] = render_to_string('behuizing.html', {'Componenten': behuizingen, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page }, context_instance=RequestContext(request))
        json = dumps(json)
        return HttpResponse(json,content_type="application/json")
    else:
        return render_to_response('behuizing.html', {'Componenten': behuizingen, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page },
                              context_instance=RequestContext(request))

def geheugen(request):

    # Get all posts from DB
    # Aantal per pagina en pagina nummer
    minPriceSliderValue = 1500.1
    maxPriceSliderValue = 0.1

    geheugenlijst = Geheugen.objects

    #overgebleven componentenlijst afhankelijk van stock
    #Dit dient later afhaneklijk te worden van alle filters
    geheugenlijst = filters(request,geheugenlijst)
    geheugen = listing(request, geheugenlijst, 15)
    
    bereik, diff, current_page = paginas(geheugenlijst, geheugen)

    if request.method == 'POST':
        json = {}
        json['Componenten'] = render_to_string('geheugen.html', {'Componenten': geheugen, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page }, context_instance=RequestContext(request))
        json = dumps(json)
        return HttpResponse(json,content_type="application/json")
    else:
        return render_to_response('geheugen.html', {'Componenten': geheugen, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page },
                              context_instance=RequestContext(request))

def gpu(request):

    # Get all posts from DB
    # Aantal per pagina en pagina nummer
    minPriceSliderValue = 1500.1
    maxPriceSliderValue = 0.1


    grafischelijst = Grafische.objects

    #overgebleven componentenlijst afhankelijk van stock
    #Dit dient later afhaneklijk te worden van alle filters
    grafischelijst = filters(request,grafischelijst)
    grafische = listing(request, grafischelijst, 15)
    
    bereik, diff, current_page = paginas(grafischelijst, grafische)

    if request.method == 'POST':
        json = {}
        json['Componenten'] = render_to_string('gpu.html', {'Componenten': grafische, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page }, context_instance=RequestContext(request))
        json = dumps(json)
        return HttpResponse(json,content_type="application/json")
    else:
        return render_to_response('gpu.html', {'Componenten': grafische, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page },
                              context_instance=RequestContext(request))
def hardeschijf(request):

    # Get all posts from DB
    # Aantal per pagina en pagina nummer
    minPriceSliderValue = 1500.1
    maxPriceSliderValue = 0.1

    hardelijst = Harde.objects

    #overgebleven componentenlijst afhankelijk van stock
    #Dit dient later afhaneklijk te worden van alle filters
    hardelijst = filters(request,hardelijst)
    harde = listing(request, hardelijst, 15)

    bereik, diff, current_page = paginas(hardelijst, harde)

    if request.method == 'POST':
        json = {}
        json['Componenten'] = render_to_string('hardeschijf.html', {'Componenten': harde, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page }, context_instance=RequestContext(request))
        json = dumps(json)
        return HttpResponse(json,content_type="application/json")
    else:
        return render_to_response('hardeschijf.html', {'Componenten': harde, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page },
                              context_instance=RequestContext(request))

def koeling(request):

    # Get all posts from DB
    # Aantal per pagina en pagina nummer
    minPriceSliderValue = 1500.1
    maxPriceSliderValue = 0.1

    koelinglijst = Koeling.objects

    #overgebleven componentenlijst afhankelijk van stock
    #Dit dient later afhaneklijk te worden van alle filters
    koelinglijst = filters(request,koelinglijst)
    koeling = listing(request, koelinglijst, 15)
    
    bereik, diff, current_page = paginas(koelinglijst, koeling)

    if request.method == 'POST':
        json = {}
        json['Componenten'] = render_to_string('koeling.html', {'Componenten': koeling, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page }, context_instance=RequestContext(request))
        json = dumps(json)
        return HttpResponse(json,content_type="application/json")
    else:
        return render_to_response('koeling.html', {'Componenten': koeling, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page },
                              context_instance=RequestContext(request))

def moederborden(request):

    # Get all posts from DB
    # Aantal per pagina en pagina nummer
    minPriceSliderValue = 1500.1
    maxPriceSliderValue = 0.1

    moederbordenlijst = Moederborden.objects

    #overgebleven componentenlijst afhankelijk van stock
    #Dit dient later afhaneklijk te worden van alle filters
    moederbordenlijst = filters(request,moederbordenlijst)
    moederborden = listing(request, moederbordenlijst, 15)
    
   
    bereik, diff, current_page = paginas(moederbordenlijst, moederborden)

    if request.method == 'POST':
        json = {}
        json['Componenten'] = render_to_string('moederbord.html', {'Componenten': moederborden, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page }, context_instance=RequestContext(request))
        json = dumps(json)
        return HttpResponse(json,content_type="application/json")
    else:
        return render_to_response('moederbord.html', {'Componenten': moederborden, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page },
                              context_instance=RequestContext(request))

def optischeschijf(request):

    # Get all posts from DB
    # Aantal per pagina en pagina nummer
    minPriceSliderValue = 1500.1
    maxPriceSliderValue = 0.1

    dvdlijst = Dvd.objects

    #overgebleven componentenlijst afhankelijk van stock
    #Dit dient later afhaneklijk te worden van alle filters
    dvdlijst = filters(request,dvdlijst)
    dvd = listing(request, dvdlijst, 15)


    bereik, diff, current_page = paginas(dvdlijst, dvd)

    if request.method == 'POST':
        json = {}
        json['Componenten'] = render_to_string('optischeschijf.html', {'Componenten': dvd, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page }, context_instance=RequestContext(request))
        json = dumps(json)
        return HttpResponse(json,content_type="application/json")
    else:
        return render_to_response('optischeschijf.html', {'Componenten': dvd, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page },
                              context_instance=RequestContext(request))


def voedingen(request):

    # Get all posts from DB
    # Aantal per pagina en pagina nummer
    minPriceSliderValue = 1500.1
    maxPriceSliderValue = 0.1

    voedinglijst = Voeding.objects

    #overgebleven componentenlijst afhankelijk van stock
    #Dit dient later afhaneklijk te worden van alle filters
    voedinglijst = filters(request,voedinglijst)
    voeding = listing(request, voedinglijst, 15)

    bereik, diff, current_page = paginas(voedinglijst, voeding)

    if request.method == 'POST':
        json = {}
        json['Componenten'] = render_to_string('voeding.html', {'Componenten': voeding, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page }, context_instance=RequestContext(request))
        json = dumps(json)
        return HttpResponse(json,content_type="application/json")
    else:
        return render_to_response('voeding.html', {'Componenten': voeding, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue, "page":current_page },
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

def build(request):
    buildpc();


