function searchInDjango(query) {
	
		$.ajax({
		//huidige pagina url
		url : window.location.pathname,
		method: "POST",
		//value van checkbox wordt meegegeven onder stock
		data: {search: query},
    })
	.done(function(data){
		var html = $(data.filterComponents).find("#productList").html();
		$('#productList').html(html);
		
	})
};

