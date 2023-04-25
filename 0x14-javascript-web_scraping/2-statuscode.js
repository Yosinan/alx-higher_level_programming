#!/usr/bin/node
// script that display the status code of a GET request
const { argv } = require('process');
const request = require('request');

const link = argv[2];
request(link, function (err, response) {
  if (err) console.log(err);
  else console.log('code:', response.statusCode);
});
