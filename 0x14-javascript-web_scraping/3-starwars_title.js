#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode number matches a given integer
const { argv } = require('process');
const request = require('request');
const id = argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
request(url, function (err, response) {
  if (err) console.log(err);
  else {
    const toJson = JSON.parse(response.body);
    console.log(toJson.title);
  }
});
