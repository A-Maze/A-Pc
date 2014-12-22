function searchInDjango(query) {
	$('#seach').value
		$.ajax({
		//huidige pagina url
		url : '/search/',
		method: "POST",
		//value van checkbox wordt meegegeven onder stock
		data: {search: query},
    })
	.done(function(data){

	})
};

