function show(which){
	if(show == "first"){
		$("#mainfirst").show();
		$("#mainsecond").hide();
	}
	else if(show == "second"){
		$("#mainfirst").hide();
		$("#mainsecond").show();
	};
};