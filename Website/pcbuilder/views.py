from django.shortcuts import render_to_response
from django.shortcuts import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.template import loader
from django.http import HttpResponse
from models import Processoren, Moederborden, Koeling, Behuizingen, Grafische, Harde, Dvd, Geheugen, Voeding
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
    return render_to_response('index.html',
                              context_instance=RequestContext(request))

def contact(request):
    msg = 1
    if request.is_ajax():
        try:
            msg = request.POST['msg']
        except:
            return HttpResponse(simplejson.dumps({'message':'Error From Server'}))
        print msg
        contact(request)
    else:
        #return HttpResponse(simplejson.dumps({'message':'Not an ajax request'}))
        return render_to_response('contact.html', {'message': msg})

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
    product = request.GET.get('product')
    categorie = request.GET.get('categorie')
    prijs = request.GET.get('prijs')
    productid = request.GET.get('productid')
    categorie.replace(" ", "")
    categorie.replace(",", "")
    prijs.replace(" ","")
    request.session[categorie] = True
    productstring = categorie + "naam"
    categorieprijs = categorie + "prijs"
    categorieid = categorie + "id"
    request.session[productstring] = product
    request.session[categorieprijs] = prijs
    request.session[categorieid] = productid
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
    
    return render_to_response('detail.html', {'Componenten': (categorieObject.objects,), 'Categorie' : categorie.lower(), 'Product': product, 'Prijs': prijs, 'Productid': productid},
context_instance=RequestContext(request))

def processoren(request):

    # Get all posts from DB
    # Aantal per pagina en pagina nummer

    minPriceSliderValue = 1500
    maxPriceSliderValue = 0

    processorenlijst = Processoren.objects


    #levering afhankelijk van filters
    levering = filters(request)
    
    #overgebleven componentenlijst afhankelijk van stock
    #Dit dient later afhaneklijk te worden van alle filters
    processorenlijst = stock(Processoren.objects, levering)

    for processoren in processorenlijst:
        #
        diestringnaam = processoren.prijs[0]
        if float(diestringnaam) < float(minPriceSliderValue):
            minPriceSliderValue = diestringnaam
        elif float(diestringnaam) > float(maxPriceSliderValue):
            maxPriceSliderValue = diestringnaam

    processoren = listing(request, processorenlijst, 15)
    #processoren = json.dumps(list(uniArray))
    
    bereik, diff = paginas(processorenlijst, processoren)

    print "werkt bijna"
    return render_to_response('processoren.html', {'Componenten': processoren, 'Range':bereik, 'Diff':diff, "minPriceSliderValue":minPriceSliderValue , "maxPriceSliderValue":maxPriceSliderValue },
                              context_instance=RequestContext(request))

def behuizingen(request):

    # Get all posts from DB
    # Aantal per pagina en pagina nummer


    behuizingenlijst = Behuizingen.objects
    behuizingen = listing(request, behuizingenlijst, 15)

    
    bereik, diff = paginas(behuizingenlijst, behuizingen)



    return render_to_response('behuizing.html', {'Componenten': behuizingen, 'Range':bereik, 'Diff':diff},
                              context_instance=RequestContext(request))

def geheugen(request):

    # Get all posts from DB
    # Aantal per pagina en pagina nummer


    geheugenlijst = Geheugen.objects
    geheugen = listing(request, geheugenlijst, 15)

    
    bereik, diff = paginas(geheugenlijst, geheugen)



    return render_to_response('geheugen.html', {'Componenten': geheugen, 'Range':bereik, 'Diff':diff},
                              context_instance=RequestContext(request))

def gpu(request):

    # Get all posts from DB
    # Aantal per pagina en pagina nummer


    grafischelijst = Grafische.objects
    grafische = listing(request, grafischelijst, 15)

    
    bereik, diff = paginas(grafischelijst, grafische)



    return render_to_response('gpu.html', {'Componenten': grafische, 'Range':bereik, 'Diff':diff},
                              context_instance=RequestContext(request))
def hardeschijf(request):

    # Get all posts from DB
    # Aantal per pagina en pagina nummer


    hardelijst = Harde.objects
    harde = listing(request, hardelijst, 15)

    
    bereik, diff = paginas(hardelijst, harde)



    return render_to_response('hardeschijf.html', {'Componenten': harde, 'Range':bereik, 'Diff':diff},
                              context_instance=RequestContext(request))

def koeling(request):

    # Get all posts from DB
    # Aantal per pagina en pagina nummer


    koelinglijst = Koeling.objects
    koeling = listing(request, koelinglijst, 15)

    
    bereik, diff = paginas(koelinglijst, koeling)



    return render_to_response('koeling.html', {'Componenten': koeling, 'Range':bereik, 'Diff':diff},
                              context_instance=RequestContext(request))

def moederborden(request):

    # Get all posts from DB
    # Aantal per pagina en pagina nummer
    moederbordenlijst = Moederborden.objects
    moederborden = listing(request, moederbordenlijst, 15)
    
   
    bereik, diff = paginas(moederbordenlijst, moederborden)



    return render_to_response('moederbord.html', {'Componenten': moederborden, 'Range':bereik, 'Diff':diff},
                              context_instance=RequestContext(request))

def optischeschijf(request):

    # Get all posts from DB
    # Aantal per pagina en pagina nummer


    dvdlijst = Dvd.objects
    dvd = listing(request, dvdlijst, 15)


    bereik, diff = paginas(dvdlijst, dvd)



    return render_to_response('optischeschijf.html', {'Componenten': dvd, 'Range':bereik, 'Diff':diff},
                              context_instance=RequestContext(request))

def voedingen(request):

    # Get all posts from DB
    # Aantal per pagina en pagina nummer


    voedinglijst = Voeding.objects
    voeding = listing(request, voedinglijst, 15)

    bereik,diff = paginas(voedinglijst, voeding)



    return render_to_response('voeding.html', {'Componenten': voeding, 'Range':bereik, 'Diff':diff},
                              context_instance=RequestContext(request))


def listing(request, componentenlijst, aantal):
    paginator = Paginator(componentenlijst,15)
    pagina = request.GET.get('pagina')

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

    return bereik, diff

def filters(request):
    #checkt of stock filter checked is
    if request.method == 'POST':
        #leveringsfilter afhankelijk van checkboxes
        print "meh"
        levering = "morgen"
        return levering
    #anders alles meegeven
    else:
        levering = "alles"
        return levering


def stock(objectlijst, levering):
    if levering == "alles":
        print "not changed"
        return objectlijst
    if levering == "morgen":
        print "changed"
        objectlijst.filter(stock__icontains="Direct leverbaar")
        return objectlijst.filter(stock__icontains="Direct leverbaar")
        






