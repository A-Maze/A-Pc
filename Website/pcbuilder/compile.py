from models import Processoren, Moederborden, Koeling, Behuizingen, Grafische, Harde, Dvd, Geheugen, Voeding, Views, Select, ViewsPerDatum
from pcbuilder.compatibility import *
from mongoengine import Q
import json

#Don't allow components without price,name or stock
data = [Processoren,Moederborden,Koeling,Behuizingen,Grafische,Harde,Dvd,Geheugen,Voeding]
dataFiltered = {}
def FilterDataset():
	#make a filtered dictionary with only the right components
	for model in data:
	    categorieNaam = model.__name__
	    filteredModel = model.objects.filter((Q(prijs__exists=True) & Q(naam__exists=True) & Q(stock__exists=True)))
	    dataFiltered[categorieNaam] = filteredModel


def buildpc(request):
	FilterDataset()
	#list with every part it should compile
	filteredDrops = request.POST.get('dropDowns')
	filteredDrops = json.loads(filteredDrops)

	for dataset in dataFiltered:
		#filter based on given requirements
		if "Processoren" in dataset:
			print "Processoren"
			(firstRequirement, secondRequirement) = (filteredDrops["#processorenSocket"],filteredDrops["#processorenCores"])
			dataFiltered[dataset] = dataFiltered[dataset].filter(Q(Socket__icontains=firstRequirement) & Q(Aantal_cores__icontains=secondRequirement))
			print dataFiltered[dataset]
		elif "Moederborden" in dataset:
			print "Moederborden"
			print "Categorie HIERBOVEN"
			(firstRequirement, secondRequirement) = (filteredDrops["#moederbordenSocket"],filteredDrops["#moederbordenChipset"])
			print firstRequirement
			print secondRequirement
			dataFiltered[dataset] = dataFiltered[dataset].filter(Q(Socket__icontains=firstRequirement) & Q(Moederbordchipset__icontains=secondRequirement))
		elif "Grafische" in dataset:
			print "Grafische"
			#(firstRequirement, secondRequirement) = (filteredDrops["#grafischeChipFabrikant"],filteredDrops["#grafischeGeheugengrootte"])
			#dataFiltered[dataset] = dataFiltered[dataset].filter(Q(Videochipfabrikant__icontains=firstRequirement) & Q(Geheugengrootte__icontains=secondRequirement))
		elif "Geheugen" in dataset:
			firstRequirement = filteredDrops["#geheugenType"]
			dataFiltered[dataset] = dataFiltered[dataset].filter(Geheugentype__icontains=firstRequirement)

		#if a selection is not found
		if not dataFiltered[dataset]:
			pass
		autoSelect(request,dataFiltered[dataset])



def autoSelect(request,componentList):
	if componentList:
		componentList = compatibility(request, componentList)
		categorie = componentList[0].categorie
		print categorie
		#get all the necesarry field names
		productstring = categorie + "naam"
		categorieprijs = categorie + "prijs"
		categorieid = categorie + "id"
		categorieherkomst = categorie + "herkomst"
		categorielink = categorie + "link"
		prijzen,naam,herkomst = convert(componentList[0].prijs,componentList[0].naam,componentList[0].herkomst)
		#assign the chosen component to the session variables
		request.session[categorie] = True
		request.session[productstring] = naam[0].replace("+", "")
		request.session[categorieprijs] = prijzen[0]
		request.session[categorieid] = str(componentList[0].id)
		request.session[categorieherkomst] = herkomst[0]
		request.session[categorielink] = componentList[0].link


def convert(prijzen,naam,herkomst):
	#make sure prices are ordered together with their origin
	prijzen = [float(x) for x in prijzen]
	herkomst = [str(x) for x in herkomst]
	merge = sorted(zip(prijzen,herkomst))
	newprijzen = [x[0] for x in merge]
	newherkomst = [x[1] for x in merge]
	print newprijzen, naam, newherkomst
	return newprijzen,naam,newherkomst