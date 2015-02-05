$(document).ready(function(){
$('.list-group-item > div:first-child').each(function() {
var eanOriginal = this.id;

ean = eanOriginal.replace(/ /g , "+")

var iURL = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + ean;
console.log(iURL)

$.ajax({
    url: iURL,
    dataType: "jsonp",
    success: function(data) {
        var imgURL = data.responseData.results[0].tbUrl
        var img = "<img src='" + imgURL + "' alt='icon'/>"
        selector = $("[id='"+eanOriginal+"']")
        console.log(selector)
        selector.html(img); 
    }
});
});
});
