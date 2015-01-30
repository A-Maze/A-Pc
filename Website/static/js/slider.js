$(document).ready(function(){
  $(".toggle").click(function(){
  var parent = $(this).parent();
  var child = parent.children(".body-toggled");
    $(child).slideToggle(100);
  var pull = $(this).children(".pull-right ");
  var switcher = $(pull).children(".switcher ");
  $(switcher).toggleClass("dropup");
  });

var minimaal = {{minPriceSliderValue}}
var maximaal = {{maxPriceSliderValue}}

$('.slider').noUiSlider({
    start: [minimaal , maximaal ],
    connect: true,

    format: wNumb({
        mark: ',',
        decimals: 1
    }),
    
    range: {
        'min': minimaal,
        'max': maximaal
    }
});

$('.slider').Link('lower').to($('#sliderMinValue'));
$('.slider').Link('upper').to($('#sliderMaxValue'));

});