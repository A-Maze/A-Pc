function filter(page) {
	//ajax afhandeling

	$.ajax({

	if (!page) {
		page = $("#active-page").text();
	} else {
		page = page;
	}

	data = {
		//huidige pagina url
		url : window.location.pathname,
		method: "POST",
		//value van checkbox wordt meegegeven onder stock
		data: {
			stock : $('#stockCheck').val(),
			minprijs: $('#sliderMinValue').val(), 
			maxprijs: $('#sliderMaxValue').val(), 
			pageNumber: page, 
			order: $("#sort-by").val(),
		},
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

function checkboxValue(page) { 
	//veranderd de value
	if($('#stockCheck').val() == "morgen"){
		$('#stockCheck').val("alles");
	}
	else{
		$('#stockCheck').val("morgen");
	}
	filter(page)
}

function sortBy(val) {
	$.ajax({
		url: window.location.pathname,
		method: "POST",
		data: { order: val},
	})
	.done(function(){
		//random shizzle here
	})
}
