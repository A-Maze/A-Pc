from models import Processoren, Moederborden, Koeling, Behuizingen, Grafische, Harde, Dvd, Geheugen, Voeding
from pcbuilder.compatibility import *
import json

def buildpc(request):
	#list with every part it should compile
	data = [Processoren, Moederborden, Koeling, Behuizingen, Grafische, Harde, Dvd, Geheugen, Voeding]
	filteredDrops = request.POST.get('dropDowns', 'empty')
	filteredDrops = json.loads(filteredDrops)
	#make sure filtered drops is not empty
	if (filteredDrops != "empty"):
		#Make sure the querysets only contain components with prices
		processor = Processoren.objects.filter(prijs__exists=True)
		moederbord = Moederborden.objects.filter(prijs__exists=True)
		geheugen = Geheugen.objects.filter(prijs__exists=True)
		#loop through filter requirements
		for requirement in filteredDrops:
			print requirement
			filterRequirement = unicode(requirement[1])
			#for every processoren requirement
			if "processoren" in requirement[0]:
				if "Socket" in requirement[0]:
					print "requirement"
					processor = processor.filter(Socket__icontains= filterRequirement)
				if "Cores" in requirement[0]:
					processor = processor.filter(Aantal_cores_icontains= filterRequirement)
				data.remove(Processoren)
				autoSelect(request,processor)

			#for every moederborder requirement
			if "moederborden" in requirement[0]:
				if "Socket" in requirement[0]:
					moederbord = moederbord.filter(Socket__icontains=filterRequirement)
				if "Chipset" in requirement[0]:
					moederbord = moederbord.filter(Moederbordchipset__icontains=filterRequirement)
				data.remove(Moederborden)
				autoSelect(request,moederbord)

			if "grafische" in requirement[0]:
				if "ChipFabrikant" in requirement[0]:
					grafische = grafische.filter(Videochipfabrikant__icontains=filterRequirement)
				if "Geheugengrootte" in requirement[0]:
					grafische = grafische.filter(Geheugengrootte__icontains=filterRequirement)
				data.remove(Grafische)
				autoSelect(request,grafische)





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