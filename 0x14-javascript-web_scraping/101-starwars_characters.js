#!/usr/bin/node
//  script that prints all characters of a Star Wars movie
const request = require('request');
const movieId = process.argv[2];
const filmList = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(filmList, function (err, res) {
  if (err) console.log(err);
  else {
    const data = JSON.parse(res.body).characters;
    const charArr = [];
    data.forEach(function (d) {
      request(d, function (err, res) {
        if (err) console.log(err);
        else {
          const chars = JSON.parse(res.body);
          charArr.push(chars.name);
        }
      });
    });
    charArr.forEach(console.log);
  }
});
