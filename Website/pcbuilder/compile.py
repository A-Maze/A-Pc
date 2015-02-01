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

	for dataset in dataFiltered:
		if "Processoren" in dataset:
			(firstRequirement, secondRequirement) = (filteredDrops["#processorenSocket"],filteredDrops["#processorenCores"])
			#dataFiltered[dataset] = dataFiltered[dataset].filter(Q(Socket__icontains=firstRequirement) and Q(Aantal_cores_icontains=secondRequirement))
			dataFiltered[dataset] = dataFiltered[dataset].filter(Aantal_cores_icontains=secondRequirement)
			print dataFiltered[dataset]
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