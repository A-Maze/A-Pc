$(document).ready(function(){
	$('#stockCheck').click(stock());

});

function stock(){
	console.log("stock getting called")
	$.ajax({
		url : $(this).attr('action'),
		method: "POST",
		data: {stock : $('#stockCheck').val()},
		succes: console.log("success")
	});
};




