function filter(page, query) {
	//ajax afhandeling
	
	if (!page || page == "") {
		page = $("#active-page").text();
	} else {
		page = page;
	}

	if (onSearchPage()) {
		if (page == "") {
			page = 1
		}

		if (query === undefined) {
			query = document.getElementById("search").value;
		}

		data = {
			//huidige pagina url
			url : window.location.pathname,
			method: "POST",
			//value van checkbox wordt meegegeven onder stock
			data: {
				pageNumber: page,
				search: query,

			},
	    }
	} else {
		merken = getMerken()

		data = {
			//huidige pagina url
			url : window.location.pathname,
			method: "POST",
			//value van checkbox wordt meegegeven onder stock
			data: {
				stockDirect : $('#direct').val(),
				stockWeek : $('#binnen-week').val(),
				minPrijs: $('#sliderMinValue').val(), 
				maxPrijs: $('#sliderMaxValue').val(), 
				pageNumber: page, 
				merken: merken,
				order: $("#sort-by").val(),
			},
	    }
    }

    console.log(data)

	//ajax afhandeling
	$.ajax(data)
	.done(function(data){
		
		var html = $(data.Componenten).find("#productList").html();
		$('#productList').html(html);

		var filter = $(data.Componenten).find("#stockCheck").attr('onclick');
		$("#stockCheck").removeAttr('onclick')
		$("#stockCheck").attr('onclick', filter)
	})
};

function checkboxValue(page, id) { 
	selector = $('#' + id)

	if (selector.val() == "true") {
		selector.val(false)
	} else {
		selector.val(true)
	}
	
	filter(page)
}

function getMerken() {
	var merken = $(".merk:checkbox:checked").map(function(){
    	return $(this).val()
    }).get()

	return merken
}

function onSearchPage() {
	if (window.location.pathname == "/search/") {
		return true
	} else {
		return false
	}
}

