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