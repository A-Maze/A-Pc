var dropId = ["#processorSocket","#processorCores", "#moederbordSocket", "#moederbordChipset", "#grafischeChipFabrikant", "#grafischeGeheugengrootte", "#geheugenType"]
function autoCompile(){
	var filteredDrops = [];
	var value;
	for (var i = 0; i<dropId.length; i++){
		value = $(dropId[i]).val();
		if (value != "0"){
			filteredDrops.push([dropId[i],value]);
		}
	}
	redirect(JSON.stringify(filteredDrops));
}

function redirect(filteredDrops){
	console.log(filteredDrops);
	data = {
		url : /compile/,
		method: "POST",
		data: {
			dropDowns : filteredDrops,
		},
    }
    

	//ajax afhandeling
	console.log(data.data)
	$.ajax(data)
	.done(function(data){
	})
}