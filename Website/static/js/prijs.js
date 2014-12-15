$(document).ready(function(){
    $('.prijs').each(function(i) {
        var prijs = $(this).text()
        var prijsArray = prijs.split('.')
        var decimal = prijsArray[1].substring(0,2)
        if (decimal.toString().length == 1) {
            decimal += 0
        }
        var prijs = "€" + prijsArray[0] + "," + decimal
        $(this).html(prijs)
    });
});