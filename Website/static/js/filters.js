$(document).ready(function(){
	//Verbind de stock function on click aan stock checkbox.
	$('#stockCheck').click(stock());

});

function stock(){
	//check of het wordt aangeroepen
	console.log("stock getting called")

	//ajax afhandeling
	$.ajax({
		//huidige pagina url
		url : $(this).attr('action'),
		method: "POST",
		//value van checkbox wordt meegegeven onder stock
		data: {stock : $('#stockCheck').val()},
		succes: console.log("success")
	});
};




