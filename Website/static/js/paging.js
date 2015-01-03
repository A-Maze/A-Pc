function pagineren(page,direction){
	if (direction == "forward" || direction == "back"){
		url = document.URL
		current = parseInt(url.substr(url.length - 1));
		if (direction == "forward" && current != 5){
			window.location = "?pagina=" + (current + 1);
		}
		else if(direction == "back" && current > 1){
			window.location = "?pagina=" + (current - 1);
		}

		
		else{
			window.location = "?pagina=" + current;
		}
		
	}
	else{
	window.location = "?pagina=" + page;
	
}
};