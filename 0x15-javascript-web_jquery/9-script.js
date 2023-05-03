$.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (Json) { 
	   $('div#hello').text(Json.hello); 
});
