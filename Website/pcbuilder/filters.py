from pcbuilder.compatibility import *
import types
from mongoengine import Q
import operator

'''def filters(request, objectlijst): 
    #filters the objectlist on compatibility first
    
    #checkt of stock filter checked is'''


def filters(request, objectlijst): 
    objectlijst = compatibility(request,objectlijst)
    if request.method == 'POST':

        direct = request.POST.get('stockDirect')
        binnenWeek = request.POST.get('stockWeek')
        sort = request.POST.get('order')
        minPrijs = request.POST.get('minPrijs')
        maxPrijs = request.POST.get('maxPrijs')
        merken = request.POST.getlist('merken[]')

        objectlijst = sorteer(objectlijst, sort)
        objectlijst = pricefilter(objectlijst, minPrijs, maxPrijs)
        objectlijst = stock(objectlijst, direct, binnenWeek)

        if len(merken) > 0:
            objectlijst = filterMerken(objectlijst, merken)

    merken = getMerken(request)

    return objectlijst, merken

def stock(objectlijst, direct, binnenWeek):
    direct_leverbaar = [
        "1 stuk op voorraad",
        "2 stuks op voorraad",
        "3 stuks op voorraad",
        "4 stuks op voorraad",
        "5 stuks op voorraad",
        "5+ stuks op voorraad",
        "Direct leverbaar",
    ]

    binnen_week = [
        "Verwacht over 6 dag(en)",
        "Verwacht over 5 dag(en)",
        "Verwacht over 4 dag(en)",
        "Verwacht over 3 dag(en)",
        "Verwacht over 2 dag(en)",
        "Verwacht over 1 dag(en)",
        "Verwacht over 1 dag",
    ]

    if direct == "true" and binnenWeek == "true":
        objectlijst = objectlijst.filter(Q(stock__in = direct_leverbaar) | Q(stock__in = binnen_week))
    else:
        if direct == "true":
            objectlijst = objectlijst.filter(stock__in = direct_leverbaar)

        if binnenWeek == "true":
            objectlijst = objectlijst.filter(stock__in = binnen_week)

    return objectlijst


def sorteer(objectlijst, sort):
    if sort == "titel-op":
        objectlijst_filtered = objectlijst.order_by('naam')
    elif sort == "titel-af":
        objectlijst_filtered = objectlijst.order_by('-naam')
    elif sort == "prijs-op":
        objectlijst_filtered = objectlijst.order_by('prijs')
    elif sort == "prijs-af":
        objectlijst_filtered = objectlijst.order_by('-prijs')
    else:
        objectlijst_filtered = objectlijst

    return objectlijst_filtered


def pricefilter(objectlijst, minPrijs, maxPrijs):
    minPrijs = minPrijs.replace(',','.')
    maxPrijs = maxPrijs.replace(',','.')

    objectlijst_filtered = objectlijst.filter(prijs__lte = maxPrijs)
    objectlijst_filtered = objectlijst_filtered.filter(prijs__gte = minPrijs)

    return objectlijst_filtered

def filterMerken(objectlijst, merken):
    query = reduce(operator.or_, (Q(naam__icontains=x) for x in merken))
    objectlijst = objectlijst.filter(query)

    return objectlijst

def getGrenzen(objectlijst):
    minPriceSliderValue = 1000.1
    maxPriceSliderValue = 0.1

    for obj in objectlijst:
        if obj.prijs:
            try:
                prijsje = obj.prijs[0]
            except KeyError:
                prijsje = obj.prijs



            for prijs in obj.prijs:
                if prijs < float(minPriceSliderValue):
                    prijsje = prijs
                elif prijs > float(maxPriceSliderValue):
                    prijsje = prijs

            if float(prijsje) < float(minPriceSliderValue):
                minPriceSliderValue = prijsje
            elif float(prijsje) > float(maxPriceSliderValue):
                maxPriceSliderValue = prijsje

    return minPriceSliderValue, maxPriceSliderValue


def getMerken(request):
    categorie = request.path

    if categorie == "/processoren/":
        merken = [
            "Intel",
            "AMD",
        ]
    elif categorie == "/moederborden/":
        merken = [
            "Asus",
            "ASRock",
            "Gigabyte",
            "MSI",
        ]
    elif categorie == "/gpu/":
        merken = [
            "Asus",
            "MSI",
            "AMD",
            "Gigabyte",
            "EVGA",
        ]
    elif categorie == "/hardeschijven/":
        merken = [
            "Hitachi",
            "Seagate",
            "HP",
            "Toshiba",
            "Samsung",
            "Crucial",
            "Kingston",
            "Transcend",
        ]
    elif categorie == "/optischeschijven/":
        merken = [
            "Asus",
            "HP",
            "Samsung",
            "LG",
        ]
    elif categorie == "/koelingen/":
        merken = [
            "Cooler Master",
            "Corsair",
            "Noiseblocker",
            "Scynthe",
        ]
    elif categorie == "/geheugen/":
        merken = [
            "Corsair",
            "Crucial",
            "Kingston",
            "Transcend",
            "G.Skill",
        ]
    elif categorie == "/voedingen/":
        merken = [
            "Antec",
            "be quiet",
            "Cooler Master",
            "Corsair",
            "Seasonic",
        ]
    elif categorie == "/behuizingen/":
        merken = [
            "Cooler Master",
            "Corsair",
            "Silverstone",
            "Aerocool",
            "Fractal Design",
        ]
    else:
        merken = []
    
    return merken
