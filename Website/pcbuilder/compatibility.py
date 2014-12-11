
def compatibility(request, objectlijst):
	categorieObject = objectlijst[0].categorie
	cookieCategorie = request.session[categorieObject]
	print categorieObject
	if cookieCategorie:
		categorieid = categorieObject + "id"
		productid = request.session[categorieid]
		component = objectlijst.filter(id=productid)
		print component

