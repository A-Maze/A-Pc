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
		succes: function(datainput){
			console.log("succes")
			var html = $(datainput).filter('#productList').html();
			$('#productList').html(html);
		}
	});
};




