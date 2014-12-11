from models import Processoren, Moederborden, Koeling, Behuizingen, Grafische, Harde, Dvd, Geheugen, Voeding
def compatibility(request, objectlijst):
	categorieObject = objectlijst[0].categorie
	if categorieObject:
		if "moederborden" in categorieObject:
			#moederbordenComp(request,objectlijst)
			pass

def moederbordenComp(request,objectlijst):
	print "moederborden called"
	if request.session["processorenid"]:
		processor = Processoren.objects.get(id=request.session["processorenid"])
		objectlijst.filter(Socket__icontains=processor.Socket)
	if request.session["behuizingenid"]:
		behuizing = Behuizingen.objects.get(id=request.session["behuizingenid"])
		objectlijst.filter(Form_factor__icontains=behuizing.Form_Factor)
