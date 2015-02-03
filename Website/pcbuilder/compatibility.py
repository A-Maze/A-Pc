from models import Processoren, Moederborden, Koeling, Behuizingen, Grafische, Harde, Dvd, Geheugen, Voeding
from mongoengine import Q

def compatibility(request, objectlijst):
	categorieObject = objectlijst[0].categorie
	if categorieObject:
		if "moederborden" in categorieObject:
			objectlijst = moederbordenComp(request,objectlijst)
		elif "processoren" in categorieObject:
			objectlijst = processorenComp(request,objectlijst)
		elif "geheugen" in categorieObject:
			objectlijst = geheugenComp(request,objectlijst)
		elif "voeding" in categorieObject:
			objectlijst = voedingComp(request,objectlijst)
		elif "grafische" in categorieObject:
			objectlijst = grafischeComp(request,objectlijst)
		elif "behuizingen" in categorieObject:
			objectlijst = behuizingenComp(request,objectlijst)
		elif "harde" in categorieObject:
			objectlijst = hardeComp(request,objectlijst)
		elif "dvd" in categorieObject:
			objectlijst = dvdComp(request,objectlijst)
		elif "koeling" in categorieObject:
			objectlijst = objectlijst
	return objectlijst

def moederbordenComp(request,objectlijst):
	firstRequirement, secondRequirement, thirdRequirement, fourthRequirement,fifthRequirement = ("","","","","")
	print "moederborden called"
	print type(objectlijst)
	if "processorenid" in request.session:
		processor = Processoren.objects.get(id=request.session["processorenid"])
		firstRequirement = processor.Socket
		print firstRequirement
	if "behuizingenid" in request.session:
		behuizing = Behuizingen.objects.get(id=request.session["behuizingenid"])
		secondRequirement = behuizing.Form_Factor[0]
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
	objectlijst_filtered = objectlijst
	if "moederbordenid" in request.session:
		moederbord = Moederborden.objects.get(id=request.session["moederbordenid"])
		objectlijst_filtered = objectlijst.filter(Socket__icontains=moederbord.Socket)
	return objectlijst_filtered

def geheugenComp(request,objectlijst):
	print "geheugen called"
	objectlijst_filtered = objectlijst
	if "moederbordenid" in request.session:
		moederbord = Moederborden.objects.get(id=request.session["moederbordenid"])
		objectlijst_filtered = objectlijst.filter(Geheugentype__icontains=moederbord.Geheugentype)
		objectlijst_filtered = objectlijst.filter(Aantal__icontains=moederbord.Geheugentype)
	return objectlijst_filtered

def voedingComp(request,objectlijst):
	print "voeding called"
	objectlijst_filtered = objectlijst
	if "moederbordenid" in request.session:
		moederbord = Moederborden.objects.get(id=request.session["voedingid"])
		#TODO be sure to check powersuply here
	return objectlijst_filtered

def grafischeComp(request,objectlijst):
	print "grafische called"
	objectlijst_filtered = objectlijst
	if "moederbordenid" in request.session:
		moederbord = Moederborden.objects.get(id=request.session["moederbordenid"])
		objectlijst_filtered = objectlijst.filter(Card_Interface__icontains=moederbord.Card_Interface)
	return objectlijst_filtered

def behuizingenComp(request,objectlijst):
	print "behuizingen called"
	objectlijst_filtered = objectlijst
	if "moederbordenid" in request.session:
		moederbord = Moederborden.objects.get(id=request.session["moederbordenid"])
		objectlijst_filtered = objectlijst.filter(Form_Factor__icontains=moederbord.Form_Factor)
	return objectlijst_filtered

def hardeComp(request,objectlijst):
	print "harde called"
	objectlijst_filtered = objectlijst
	if "moederbordenid" in request.session:
		moederbord = Moederborden.objects.get(id=request.session["moederbordenid"])
		objectlijst_filtered = objectlijst.filter(Hardeschijf_bus__icontains=moederbord.Hardeschijf_bus)
	return objectlijst_filtered

def dvdComp(request,objectlijst):
	print "dvd called"
	objectlijst_filtered = objectlijst
	if "moederbordenid" in request.session:
		moederbord = Moederborden.objects.get(id=request.session["moederbordenid"])
		objectlijst_filtered = objectlijst.filter(Hardeschijf_bus__icontains=moederbord.Hardeschijf_bus)
	return objectlijst_filtered

