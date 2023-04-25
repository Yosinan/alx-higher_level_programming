#!/usr/bin/node
//  script that prints all characters of a Star Wars movie
const request = require('request');
const movieId = process.argv[2];
const filmList = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(filmList, function (err, res) {
  if (err) console.log(err);
  else {
    const data = JSON.parse(res.body).characters;
    rec(data, 0);
  }
});

function rec (data, idx) {
	    request(data[idx], (err, res) => {
		    if (err) console.log(err);
		    else {
			    console.log(JSON.parse(res.body).name);
			    if (idx + 1 < data.length) {
				    rec(data, idx + 1);
			    }
		    }
	    });
}
