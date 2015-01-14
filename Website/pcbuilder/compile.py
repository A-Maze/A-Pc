from models import Processoren, Moederborden, Koeling, Behuizingen, Grafische, Harde, Dvd, Geheugen, Voeding
import json

def buildpc(request):
	data = [Processoren, Moederborden, Koeling, Behuizingen, Grafische, Harde, Dvd, Geheugen, Voeding]
	filteredDrops = request.POST.get('dropDowns', 'empty')
	filteredDrops = json.loads(filteredDrops)
	if (filteredDrops != "empty"):
		processor = Processoren.objects
		for requirement in filteredDrops:
			print requirement

			if "processoren" in requirement[0]:
				print "stap 2"
				if "Socket" in requirement[0]:
					print 'verder'
					processor.filter(Socket__icontains=requirement[1])
				if "Cores" in requirement[0]:
					print "nog verder"
					processor.filter(Aantal_cores_icontains=requirement[1])
				data.remove(Processoren)
				autoSelect(request,processor)

			if "Moederborden" in requirement[0]:
				moederbord = Moederborden.objects
				if "Socket" in requirement[0]:
					moederbord.filter(Socket__icontains=requirement[1])
				if "Chipset" in requirement[0]:
					moederbord.filter(Moederbordchipset__icontains=requirement[1])
				data.remove(Moederborden)
				autoSelect(request,moederbord)

		for dataset in data:
			print "loopend"
			print dataset
			autoSelect(request,dataset.objects)



def autoSelect(request,componentList):
	print "callend"
	if componentList:
		print "called sequel"
		categorie = componentList[0].categorie
		productstring = categorie + "naam"
		categorieprijs = categorie + "prijs"
		categorieid = categorie + "id"
		categorieherkomst = categorie + "herkomst"
		categorielink = categorie + "link"
		prijzen,naam,herkomst = convert(componentList[0].prijs,componentList[0].naam,componentList[0].herkomst)
		request.session[categorie] = True
		request.session[productstring] = naam[0].replace("+", "")
		request.session[categorieprijs] = prijzen[0]
		request.session[categorieid] = str(componentList[0].id)
		request.session[categorieherkomst] = herkomst[0]
		request.session[categorielink] = componentList[0].link

def convert(prijzen,naam,herkomst):
	print "prijs"
	prijzen = [float(x) for x in prijzen]
	return prijzen,naam,herkomst