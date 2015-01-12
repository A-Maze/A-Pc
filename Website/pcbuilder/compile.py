from models import Processoren, Moederborden, Koeling, Behuizingen, Grafische, Harde, Dvd, Geheugen, Voeding
import json
def buildpc(request):
	filteredDrops = request.POST.get('dropDowns', 'empty')
	filteredDrops = json.loads(filteredDrops)
	if (filteredDrops != "empty"):
		for requirement in filteredDrops:
			print requirement
			if "processor" in requirement[0]:
				processor = Processoren.objects
				print "stap 2"
				if "Socket" in requirement[0]:
					print 'verder'
					processor.filter(Socket__icontains=requirement[1])
				if "Cores" in requirement[0]:
					print "nog verder"
					processor.filter(Aantal_cores_icontains=requirement[1])
				autoSelect(processor)


def autoSelect(componentList):
	print "calledd"
	request.session[productstring] = processor[0].naam
	request.session[categorieprijs] = processor[0].prijs
	request.session[categorieid] = processor[0].id
	request.session[categorieherkomst] = processor[0].id
	request.session[categorielink] = processor[0].link
