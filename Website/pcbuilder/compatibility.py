from models import Processoren, Moederborden, Koeling, Behuizingen, Grafische, Harde, Dvd, Geheugen, Voeding
def compatibility(request, objectlijst):
	categorieObject = objectlijst[0].categorie
	if categorieObject:
		if "moederborden" in categorieObject:
			#moederbordenComp(request,objectlijst)
			pass
		elif "processoren" in categorieObject:
			#processorenComp(request,objectlijst)
			pass
		elif "geheugen" in categorieObject:
			#geheugenComp(request,objectlijst)
			pass

def moederbordenComp(request,objectlijst):
	print "moederborden called"
	if request.session["processorenid"]:
		processor = Processoren.objects.get(id=request.session["processorenid"])
		objectlijst.filter(Socket__icontains=processor.Socket)
	if request.session["behuizingenid"]:
		behuizing = Behuizingen.objects.get(id=request.session["behuizingenid"])
		objectlijst.filter(Form_factor__icontains=behuizing.Form_Factor)
	if request.session["geheugenid"]:
		geheugen = Geheugen.objects.get(id=request.session["geheugenid"])
		objectlijst.filter(Geheugentype__icontains=geheugen.Geheugentype)
		objectlijst.filter(Geheugentype__icontains=geheugen.Aantal)
	if request.session["hardeid"]:
		harde = Harde.objects.get(id=request.session["hardeid"])
		objectlijst.filter(Hardeschijf_bus__icontains=harde.Hardeschijf_bus)

def processorenComp(request,objectlijst):
	print "processoren called"
	if request.session["moederbordenid"]:
		moederbord = Moederborden.objects.get(id=request.session["moederbordenid"])
		objectlijst.filter(Socket__icontains=moederbord.Socket)

def geheugenComp(request,objectlijst):
	print "geheugen called"
	if request.session["moederbordenid"]:
		moederbord = Moederborden.objects.get(id=request.session["moederbordenid"])
		objectlijst.filter(Geheugentype__icontains=moederbord.Geheugentype)
		objectlijst.filter(Aantal__icontains=moederbord.Geheugentype)