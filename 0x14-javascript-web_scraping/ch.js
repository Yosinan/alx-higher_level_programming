#!/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/18';

request(url, function (err, res) {
  if (err) console.log(err);
  else {
    const data = JSON.parse(res.body);
    const no = data.name;
    console.log(no);
  }
});
