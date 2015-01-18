from models import Processoren, Moederborden, Koeling, Behuizingen, Grafische, Harde, Dvd, Geheugen, Voeding
def compatibility(request, objectlijst):
	categorieObject = objectlijst[0].categorie
	if categorieObject:
		if "moederborden" in categorieObject:
			objectlijst_filtered = moederbordenComp(request,objectlijst)
		elif "processoren" in categorieObject:
			objectlijst_filtered = processorenComp(request,objectlijst)
		elif "geheugen" in categorieObject:
			objectlijst_filtered = geheugenComp(request,objectlijst)
		elif "voeding" in categorieObject:
			objectlijst_filtered = voedingComp(request,objectlijst)
		elif "grafische" in categorieObject:
			objectlijst_filtered = grafischeComp(request,objectlijst)
		elif "behuizingen" in categorieObject:
			objectlijst_filtered = behuizingenComp(request,objectlijst)
		elif "harde" in categorieObject:
			objectlijst_filtered = hardeComp(request,objectlijst)
		elif "dvd" in categorieObject:
			objectlijst_filtered = dvdComp(request,objectlijst)
		elif "koeling" in categorieObject:
			objectlijst_filtered = objectlijst
	return objectlijst_filtered

def moederbordenComp(request,objectlijst):
	print "moederborden called"
	objectlijst_filtered = objectlijst
	if "processorenid" in request.session:
		processor = Processoren.objects.get(id=request.session["processorenid"])
		objectlijst_filtered = objectlijst.filter(Socket__icontains=processor.Socket)
	if "behuizingenid" in request.session:
		behuizing = Behuizingen.objects.get(id=request.session["behuizingenid"])
		objectlijst_filtered = objectlijst.filter(Form_Factor__icontains=behuizing.Form_Factor)
		print objectlijst_filtered
	if "geheugenid" in request.session:
		geheugen = Geheugen.objects.get(id=request.session["geheugenid"])
		objectlijst_filtered = objectlijst.filter(Geheugentype__icontains=geheugen.Geheugentype)
		objectlijst_filtered = objectlijst.filter(Geheugentype__icontains=geheugen.Aantal)
	if "hardeid" in request.session:
		harde = Harde.objects.get(id=request.session["hardeid"])
		objectlijst_filtered = objectlijst.filter(Hardeschijf_bus__icontains=harde.Hardeschijf_bus)
	return objectlijst_filtered

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

