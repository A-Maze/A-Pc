from models import Processoren, Moederborden, Koeling, Behuizingen, Grafische, Harde, Dvd, Geheugen, Voeding
from mongoengine import Q


print "ja"
def compatibility(request, objectlijst):
	categorieObject = objectlijst[0].categorie
	if categorieObject:
		if "moederborden" in categorieObject:
			objectlijst = moederbordenComp(request,objectlijst)
		elif "processoren" in categorieObject:
			objectlijst = processorenComp(request,objectlijst)
		elif "geheugen" in categorieObject:
			objectlijst = geheugenComp(request,objectlijst)
		elif "grafische" in categorieObject:
			objectlijst = grafischeComp(request,objectlijst)
		elif "behuizingen" in categorieObject:
			objectlijst = behuizingenComp(request,objectlijst)
		elif "harde" in categorieObject:
			objectlijst = hardeComp(request,objectlijst)
	return objectlijst

def moederbordenComp(request,objectlijst):
	firstRequirement, secondRequirement, thirdRequirement, fourthRequirement= ("","","","")
	if "processorenid" in request.session:
		processor = Processoren.objects.get(id=request.session["processorenid"])
		firstRequirement = [item.encode('UTF8') for item in processor.Socket]
		firstRequirement = "".join(firstRequirement)
	if "geheugenid" in request.session:
		geheugen = Geheugen.objects.get(id=request.session["geheugenid"])
		thirdRequirement = [item.encode('UTF8') for item in geheugen.Geheugentype]
		thirdRequirement = "".join(thirdRequirement)
	if "hardeid" in request.session:
		harde = Harde.objects.get(id=request.session["hardeid"])
		fourthRequirement = [item.encode('UTF8') for item in harde.Hardeschijf_bus]
		fourthRequirement = "".join(fourthRequirement)
	objectlijst = objectlijst.filter(Q(Socket__icontains=firstRequirement) & Q(Form_Factor__icontains=secondRequirement) & Q(Geheugentype__icontains=thirdRequirement) & Q(Hardeschijf_bus__icontains=fourthRequirement))
	return objectlijst

def processorenComp(request,objectlijst):
	print "processoren called"
	firstRequirement = ""
	if "moederbordenid" in request.session:
		moederbord = Moederborden.objects.get(id=request.session["moederbordenid"])
		firstRequirement = [item.encode('UTF8') for item in moederbord.Socket]
		firstRequirement = "".join(firstRequirement)
	objectlijst = objectlijst.filter(Socket__icontains=firstRequirement)
	return objectlijst

def geheugenComp(request,objectlijst):
	print "geheugen called"
	firstRequirement = ""
	if "moederbordenid" in request.session:
		moederbord = Moederborden.objects.get(id=request.session["moederbordenid"])
		firstRequirement = [item.encode('UTF8') for item in moederbord.Geheugentype]
		firstRequirement = "".join(firstRequirement)
		firstRequirement = firstRequirement[3:]

	objectlijst = objectlijst.filter(Geheugentype__icontains=firstRequirement)
	return objectlijst

def grafischeComp(request,objectlijst):
	print "grafische called"
	firstRequirement = ""
	if "moederbordenid" in request.session:
		moederbord = Moederborden.objects.get(id=request.session["moederbordenid"])
		firstRequirement = [item.encode('UTF8') for item in moederbord.Card_Interface]
		firstRequirement = "".join(firstRequirement)
	objectlijst = objectlijst.filter(Card_Interface__icontains=firstRequirement)
	return objectlijst

def behuizingenComp(request,objectlijst):
	print "behuizingen called"
	firstRequirement = ""
	if "moederbordenid" in request.session:
		moederbord = Moederborden.objects.get(id=request.session["moederbordenid"])
		firstRequirement = [item.encode('UTF8') for item in moederbord.Form_Factor]
		firstRequirement = "".join(firstRequirement)
	objectlijst = objectlijst.filter(Form_Factor__icontains=firstRequirement)
	return objectlijst

def hardeComp(request,objectlijst):
	print "harde called"
	firstRequirement = ""
	if "moederbordenid" in request.session:
		moederbord = Moederborden.objects.get(id=request.session["moederbordenid"])
		firstRequirement = [item.encode('UTF8') for item in moederbord.Hardeschijf_bus]
		firstRequirement = "".join(firstRequirement)
		firstRequirement = firstRequirement[3:]

	objectlijst = objectlijst.filter(Hardeschijf_bus__icontains=firstRequirement)
	return objectlijst

