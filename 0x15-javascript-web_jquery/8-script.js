$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (Json) {
	for (const title of Json.results) {
	$('ul#list_movies').append('<li>' + title.title + '</li>');
	}
});
