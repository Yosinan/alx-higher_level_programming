#!/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/people/18/';
const link = process.argv[2];
request(link, function (err, res, body) {
  if (err) console.log(err);
  else {
    const data = JSON.parse(body).results;
    const no = data.filter(d => d.characters.includes(url)).length;
    console.log(no);
  }
});
