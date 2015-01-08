from itertools import chain
from pcbuilder.compatibility import *
import operator
import types

def filters(request, objectlijst): 
    #filters the objectlist on compatibility first
    compatibility(request,objectlijst)   
    #checkt of stock filter checked is
    if request.method == 'POST':

        #leveringsfilter afhankelijk van checkboxes

        print objectlijst

        objectlijst1 = stock2(request, objectlijst)
        print objectlijst1

        objectlijst = sort2(request, objectlijst)
        print objectlijst2

        minprijs = request.POST.get('minprijs')
        maxprijs = request.POST.get('maxprijs')

        return objectlijst
    else:
        return objectlijst


def stock2(request, objectlijst):
    if request.POST.get('stock') == 'morgen':
        levering = request.POST.get('stock')
        return stock(objectlijst, levering)
    else:
        return objectlijst

def sort2(request, objectlijst):
    if request.POST.get('order') != "0":
        sort = request.POST.get('order')
        return sorteer(objectlijst, sort)
    else:
        return objectlijst

def stock(objectlijst, levering):
    direct_leverbaar = [
        "1 stuk op voorraad",
        "2 stuks op voorraad",
        "3 stuks op voorraad",
        "4 stuks op voorraad",
        "5 stuks op voorraad",
        "5+ stuks op voorraad",
        "Direct leverbaar"
    ]

    if levering == "alles":
        return objectlijst
    elif levering == "morgen":
        for key, d in enumerate(direct_leverbaar):
            objects = objectlijst.filter(stock__icontains=d)
            if key == 0:
                objectlijst_filtered = objects
            else:
                objectlijst_filtered = list(chain(objects, objectlijst_filtered))
        return objectlijst_filtered


def sorteer(objectlijst, sort):

    '''for o in objectlijst:
        if isinstance(o.prijs, list):
            o.prijs = o.prijs[0]
        else:
            print "nee"'''

    if sort == "titel-op":
        objectlijst_filtered = objectlijst.order_by('naam')
    elif sort == "titel-af":
        objectlijst_filtered = objectlijst.order_by('-naam')
    else:
        objectlijst_filtered = objectlijst

    #for o in objectlijst_filtered:
        #print o.naam
        #lol

    return objectlijst_filtered


def pricefilter(objectlijst, minprijs, maxprijs):
    #replaces the , in the 2 arguments with . for float parsing
    minprijs = minprijs.replace(',','.')
    maxprijs = maxprijs.replace(',','.')
    #for every component in the queryset
    print objectlijst
    newLijst = objectlijst
    for component in newLijst:
        #convert price to float
        prijs = float(component.prijs[0])
        #if the component price is not within the range of the 2 prices
        if (prijs < float(minprijs)) or (prijs > float(maxprijs)):
            #then filter that component from the queryset
            if component.ean:
                pass#hier komt magie
            elif component.sku:
                pass#hier komt magie
    return newLijst

