$(document).ready(function(){
$('.list-group-item > div:first-child').each(function() {
var ean = this.id;

var iURL = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + ean;

$.ajax({
    url: iURL,
    dataType: "jsonp",
    success: function(data) {
        var imgURL = data.responseData.results[0].tbUrl
        var img = "<img src='" + imgURL + "' alt='icon'/>"
        $("#" + ean).html(img); 
    }
});
});
});
