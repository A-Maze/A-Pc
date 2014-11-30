function stock(){
	//check of het wordt aangeroepen
	console.log("stock getting called")
	
	//ajax afhandeling
	$.ajax({
		//huidige pagina url
		url : window.location.pathname,
		method: "POST",
		//value van checkbox wordt meegegeven onder stock
		data: {stock : $('#stockCheck').val()},
    })
	.done(function(data){
		var html = $(data.Componenten).find("#productList").html();
		$('#productList').html(html);
	})

	//veranderd de value
	if($('#stockCheck').val() == "morgen"){
		$('#stockCheck').val("alles")
	}
	else{
		$('#stockCheck').val("morgen")
	}
};




