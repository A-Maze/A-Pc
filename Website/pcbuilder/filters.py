from itertools import chain

def filters(request, objectlijst):
    
    #checkt of stock filter checked is
    if request.method == 'POST':

        #leveringsfilter afhankelijk van checkboxes
        if request.POST.get('stock') == 'morgen':
            levering = request.POST.get('stock')
            objectlijst = stock(objectlijst,levering)

        minprijs = request.POST.get('minprijs')
        maxprijs = request.POST.get('maxprijs')

        return objectlijst
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

