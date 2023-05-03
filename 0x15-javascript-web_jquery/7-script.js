$.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (Json) {
	$('div#character').text(Json.name);
});
