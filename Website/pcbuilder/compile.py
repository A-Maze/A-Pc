from models import Processoren, Moederborden, Koeling, Behuizingen, Grafische, Harde, Dvd, Geheugen, Voeding
from pcbuilder.compatibility import *
import json

def buildpc(request):
	data = [Processoren, Moederborden, Koeling, Behuizingen, Grafische, Harde, Dvd, Geheugen, Voeding]
	filteredDrops = request.POST.get('dropDowns', 'empty')
	filteredDrops = json.loads(filteredDrops)
	if (filteredDrops != "empty"):
		processor = Processoren.objects.filter(prijs__exists=True)
		processor_filtered = processor
		print processor_filtered
		for requirement in filteredDrops:
			print requirement

			if "processoren" in requirement[0]:
				if "Socket" in requirement[0]:
					print "requirement"
					filterRequirement = unicode(requirement[1])

					processor_filtered = processor.filter(Socket__icontains= filterRequirement)
					if not processor_filtered:
						print "leeg"
				if "Cores" in requirement[0]:
					processor = processor.filter(Aantal_cores_icontains=requirement[1])
				data.remove(Processoren)
				autoSelect(request,processor_filtered)

			if "Moederborden" in requirement[0]:
				moederbord = Moederborden.objects.filter(prijs__exists=True)
				if "Socket" in requirement[0]:
					moederbord.filter(Socket__icontains=requirement[1])
				if "Chipset" in requirement[0]:
					moederbord.filter(Moederbordchipset__icontains=requirement[1])
				data.remove(Moederborden)
				autoSelect(request,moederbord)

		for dataset in data:
			print "looping"
			autoSelect(request,dataset.objects.filter(prijs__exists=True))



def autoSelect(request,componentList):
	if componentList:
		#componentenList = compatibility(request, componentList)
		categorie = componentList[0].categorie
		print categorie
		if "processor" in categorie:
			print "eigenlijke socket"
			print componentList[0].Socket
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
	prijzen = [float(x) for x in prijzen]
	herkomst = [str(x) for x in herkomst]
	merge = sorted(zip(prijzen,herkomst))
	newprijzen = [x[0] for x in merge]
	newherkomst = [x[1] for x in merge]
	print newprijzen, naam, newherkomst
	return newprijzen,naam,newherkomst