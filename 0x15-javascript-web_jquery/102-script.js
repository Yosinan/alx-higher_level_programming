$('input#btn_translate').click(function () {
	$.getJSON('https://fourtonfish.com/hellosalut/',{ lang: $('input#language_code').val() }, function (Json) {
		$('div#hello').text(Json.hello);}
	);
});
