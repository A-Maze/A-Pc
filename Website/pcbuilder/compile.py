from models import Processoren, Moederborden, Koeling, Behuizingen, Grafische, Harde, Dvd, Geheugen, Voeding, Views, Select, ViewsPerDatum
from pcbuilder.compatibility import *
from mongoengine import Q
import json

#Don't allow components without price,name or stock
data = [Processoren,Moederborden,Koeling,Behuizingen,Grafische,Harde,Dvd,Geheugen,Voeding]
dataFiltered = {}
def FilterDataset():
	for model in data:
	    categorieNaam = model.__name__
	    filteredModel = model.objects.filter((Q(prijs__exists=True) and Q(naam__exists=True) and Q(stock__exists=True)))
	    dataFiltered[categorieNaam] = filteredModel


def buildpc(request):
	FilterDataset()
	#list with every part it should compile
	filteredDrops = request.POST.get('dropDowns')
	filteredDrops = json.loads(filteredDrops)
	print filteredDrops
	#make sure filtered drops is not empty
	if (filteredDrops):
		print "if"

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
				del dataFiltered["Processoren"]
			

			#for every moederborder requirement
			if "moederborden" in requirement[0]:
				if "Socket" in requirement[0]:
					moederbord = moederbord.filter(Socket__icontains=filterRequirement)
				if "Chipset" in requirement[0]:
					moederbord = moederbord.filter(Moederbordchipset__icontains=filterRequirement)
				del dataFiltered["Moederborden"]
				

			if "grafische" in requirement[0]:
				if "ChipFabrikant" in requirement[0]:
					grafische = grafische.filter(Videochipfabrikant__icontains=filterRequirement)
				if "Geheugengrootte" in requirement[0]:
					grafische = grafische.filter(Geheugengrootte__icontains=filterRequirement)
				del dataFiltered["Grafische"]
			autoSelect(request,processor)
			autoSelect(request,moederbord)
			autoSelect(request,grafische)






	for dataset in dataFiltered:
		print "looping"
		autoSelect(request,dataFiltered[dataset])



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