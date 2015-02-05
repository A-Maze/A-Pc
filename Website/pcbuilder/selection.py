from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.shortcuts import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.template import loader
from django.http import HttpResponse
from dashboard import ViewsPerDag, Viewers, Selected
from models import Processoren, Moederborden, Koeling, Behuizingen, Grafische, Harde, Dvd, Geheugen, Voeding, Views, Select, ViewsPerDatum, Login, Users, Registreer, SearchQuery


def select(request):
    #getting all the variables from the url
    product = request.GET.get('product')
    categorie = request.GET.get('categorie')
    prijs = request.GET.get('prijs')
    productid = request.GET.get('productid')
    herkomst = request.GET.get('herkomst')
    link = request.GET.get('link')
    prijs = float(prijs)

    Viewers(productid, categorie, 'delete', request)
    Selected(productid, categorie, 'add', request)
    ViewsPerDag('delete', request)


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
    
    Viewers(productid, categorie, 'delete', request)
    ViewsPerDag('delete', request)

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
    ViewsPerDag('add', request)

    component = categorieObject.objects.get(id=productid)



    if(component.herkomst):
        ziplist = zip(component.herkomst, component.stock, component.link, component.prijs)


    #if currentproduct and currentherkomst exist render them to response as well
    if existing:
        return render_to_response('detail.html', {'component': component, 'Productid': productid, 'Ziplist': ziplist, 'CurrentID': currentID, 'Currentherkomst': currentherkomst })
    else:
        return render_to_response('detail.html', {'component': component, 'Productid': productid, 'Ziplist': ziplist})