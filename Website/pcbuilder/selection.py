from django.shortcuts import render_to_response
from django.shortcuts import HttpResponseRedirect
from dashboard import ViewsPerDag, Viewers, Selected
from models import Processoren, Moederborden, Koeling, Behuizingen, Grafische, Harde, Dvd, Geheugen, Voeding, Views, Select, ViewsPerDatum, Login, Users, Registreer, SearchQuery
from mongoengine import Q

data = [Processoren,Moederborden,Koeling,Behuizingen,Grafische,Harde,Dvd,Geheugen,Voeding]
dataFiltered = {}
for model in data:
    categorieNaam = model.__name__
    empty = unicode("")
    filteredModel = model.objects.filter((Q(prijs__exists=True) & Q(naam__exists=True) & Q(stock__exists=True) & Q(link__exists=True) & Q(herkomst__exists=True)))
    dataFiltered[categorieNaam] = filteredModel


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
    Selected(productid, categorie, 'add', request)
    #ViewsPerDag('delete', request)


    categorie.replace(" ", "")
    categorie.replace(",", "")
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
    if request.session[productstring] == product:
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


    
    categorieObject = dataFiltered[categorie.title()]

    #Viewers(productid, categorie, 'add', request)
    #ViewsPerDag('add', request)

    component = categorieObject.get(id=productid)



    if(component.herkomst):
        ziplist = zip(component.herkomst, component.stock, component.link, component.prijs)
    else:
        print "help"


    #if currentproduct and currentherkomst exist render them to response as well
    if existing:
        return render_to_response('detail.html', {'component': component, 'Productid': productid, 'Ziplist': ziplist, 'CurrentID': currentID, 'Currentherkomst': currentherkomst })
    else:
        return render_to_response('detail.html', {'component': component, 'Productid': productid, 'Ziplist': ziplist})