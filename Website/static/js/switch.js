function show(which){
	if(which == "first"){
		$("#mainfirst").show();
		$("#mainsecond").hide();
	}
	else if(which == "second"){
		$("#mainfirst").hide();
		$("#mainsecond").show();
	};
};

//toggles the dropdown menus
function showDrops(e){
	//finds the sibling of the element that was clicked
	var sibling = $(e).siblings('.panel-footer');
	//finds the dropdown panel in that sibling and toggles it
	sibling.children('.dropdown-panel').toggle('fast');
}