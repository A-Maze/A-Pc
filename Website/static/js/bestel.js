

function showBestel(show) {
    if (!show) {
        $('#inComplete').show()
        $('#complete').hide();
    } else {
        $('#inComplete').hid()
        $('#complete').show();
    }
}

function showLinks(e){
  $('.externalLink').toggle();
  $('.internalLink').toggle()
  if ($(e).text() == "Toon links"){
    	$(e).text("Toon namen")
    	$('#columnHeader').text("Link")
    	$(e).css("color", "#337ab7")
    }
    else{
    	$(e).text("Toon links");
    	$('#columnHeader').text("Product")
   		$(e).css("color", "rgba(0, 0, 0, 0.84)")
   	}
}