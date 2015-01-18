from itertools import chain
from pcbuilder.compatibility import *
import types
from models import Processoren
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
        #objectlijst = pricefilter(objectlijst, minPrijs, maxPrijs)
        objectlijst = stock(objectlijst, direct, binnenWeek)

        if len(merken) > 0:
            #objectlijst = filterMerken(objectlijst, merken)
            pass

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
        # Q object
        objectlijst = objectlijst.filter(stock__in = direct_leverbaar)
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
    print merken

    brand = []
    for merk in merken:
        brand.append(str(merk))

    print brand

    #objectlijst.filter(reduce(operator.and_, (Q(naam__icontains=title) for title in brand)))
    #objectlijst = objectlijst.filter(reduce(operator.and_, (Q(naam__icontains=title) for title in brand)))
    
    #query = reduce(operator.and_, (Q(naam__contains = item) for item in ['Intel', 'AMD']))


    #query = "Q(naam__contains='Intel') & Q(naam__contains='AMD')"
    #print query


    print "2"


    #objectlijst = objectlijst.filter(naam__icontains=brand[0])

    #objectlijst = objectlijst.filter(naam__contains=['Intel', 'AMD'])


    #objectlijst = objectlijst.filter(q)

    from django.db.models import Q
    from models import Processoren

    cpu = [
        "Intel",
        "AMD"
    ]

    queryset = Processoren.objects.filter(Q(naam__contains=cpu[0]) | Q(naam__contains=cpu[1]))
    queryset = Processoren.objects.filter(naam__contains=cpu[1])

    print queryset

    #objectlijst = objectlijst.filter(Q(naam__contains='Intel') | Q(naam__contains='AMD'))
    
    print "3"



    #objectlijst = objectlijst.filter(naam__icontains = merken[0])



    return objectlijst

def getGrenzen(objectlijst):
    minPriceSliderValue = 1500.1
    maxPriceSliderValue = 0.1

    for obj in objectlijst:
        if obj.prijs:
            prijsje = obj.prijs[0]

            for prijs in obj.prijs:
                if float(prijs) < float(minPriceSliderValue):
                    prijsje = prijs
                elif float(prijs) > float(maxPriceSliderValue):
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