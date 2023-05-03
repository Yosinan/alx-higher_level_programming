// function to fetch n display 
function salute () {
	$.getJSON('https://fourtonfish.com/hellosalut/',{ lang: $('input#language_code').val() }, function (Json) {
		$('div#hello').text(Json.hello);}
	);
}

// jquery to handle the btn and enter events
$(function () {
$('input#btn_translate').click(salute);
$('input#btn_translate').keydown(function (event) {
  if (event.which === 13) {
	  salute();
  }
});
});
