from models import Processoren, Moederborden, Koeling, Behuizingen, Grafische, Harde, Dvd, Geheugen, Voeding
from mongoengine import Q

def compatibility(request, objectlijst):
	categorieObject = objectlijst[0].categorie
	if categorieObject:
		if "moederborden" in categorieObject:
			objectlijst = moederbordenComp(request,objectlijst)
		# elif "processoren" in categorieObject:
		# 	objectlijst = processorenComp(request,objectlijst)
		# elif "geheugen" in categorieObject:
		# 	objectlijst = geheugenComp(request,objectlijst)
		# elif "voeding" in categorieObject:
		# 	objectlijst = voedingComp(request,objectlijst)
		# elif "grafische" in categorieObject:
		# 	objectlijst = grafischeComp(request,objectlijst)
		# elif "behuizingen" in categorieObject:
		# 	objectlijst = behuizingenComp(request,objectlijst)
		# elif "harde" in categorieObject:
		# 	objectlijst = hardeComp(request,objectlijst)
		# elif "dvd" in categorieObject:
		# 	objectlijst = dvdComp(request,objectlijst)
		# elif "koeling" in categorieObject:
		# 	objectlijst = objectlijst
	return objectlijst

def moederbordenComp(request,objectlijst):
	firstRequirement, secondRequirement, thirdRequirement, fourthRequirement,fifthRequirement = ("","","","","")
	print "moederborden called"
	print type(objectlijst)
	if "processorenid" in request.session:
		processor = Processoren.objects.get(id=request.session["processorenid"])
		firstRequirement = processor.Socket
		print "first Requirement"
		print firstRequirement
	if "behuizingenid" in request.session:
		behuizing = Behuizingen.objects.get(id=request.session["behuizingenid"])
		secondRequirement = behuizing.Form_Factor
	if "geheugenid" in request.session:
		geheugen = Geheugen.objects.get(id=request.session["geheugenid"])
		thirdRequirement = geheugen.Geheugentype
		fourthRequirement = geheugen.Aantal
	if "hardeid" in request.session:
		harde = Harde.objects.get(id=request.session["hardeid"])
		fifthRequirement = harde.Hardeschijf_bus
	objectlijst = objectlijst.filter(Q(Socket__icontains=firstRequirement) & Q(Form_Factor__icontains=secondRequirement) & Q(Geheugentype__icontains=thirdRequirement) & Q(Geheugentype__icontains=fourthRequirement) & Q(Hardeschijf_bus__icontains=fifthRequirement))
	return objectlijst

def processorenComp(request,objectlijst):
	print "processoren called"
	if "moederbordenid" in request.session:
		moederbord = Moederborden.objects.get(id=request.session["moederbordenid"])
		firstRequirement = moederbord.Socket
	objectlijst = objectlijst.filter(Socket__icontains=firstRequirement)
	return objectlijst

def geheugenComp(request,objectlijst):
	print "geheugen called"
	if "moederbordenid" in request.session:
		moederbord = Moederborden.objects.get(id=request.session["moederbordenid"])
		firstRequirement = moederbord.Geheugentype
		secondRequirement = moederbord.Geheugentype
	objectlijst = objectlijst.filter(Q(Geheugentype__icontains=firstRequirement) & Q(Aantal__icontains=secondRequirement))
	return objectlijst

def grafischeComp(request,objectlijst):
	print "grafische called"
	if "moederbordenid" in request.session:
		moederbord = Moederborden.objects.get(id=request.session["moederbordenid"])
		firstRequirement = moederbord.Card_Interface
	objectlijst = objectlijst.filter(Card_Interface__icontains=firstRequirement)
	return objectlijst

def behuizingenComp(request,objectlijst):
	print "behuizingen called"
	if "moederbordenid" in request.session:
		moederbord = Moederborden.objects.get(id=request.session["moederbordenid"])
		firstRequirement = moederbord.Form_Factor
	objectlijst = objectlijst.filter(Form_Factor__icontains=firstRequirement)
	return objectlijst

def hardeComp(request,objectlijst):
	print "harde called"
	if "moederbordenid" in request.session:
		moederbord = Moederborden.objects.get(id=request.session["moederbordenid"])
		firstRequirement = moederbord.Hardeschijf_bus
	objectlijst = objectlijst.filter(Hardeschijf_bus__icontains=firstRequirement)
	return objectlijst

def dvdComp(request,objectlijst):
	print "dvd called"
	if "moederbordenid" in request.session:
		moederbord = Moederborden.objects.get(id=request.session["moederbordenid"])
		firstRequirement = moederbord.Hardeschijf_bus
	objectlijst = objectlijst.filter(Hardeschijf_bus__icontains=firstRequirement)
	return objectlijst

