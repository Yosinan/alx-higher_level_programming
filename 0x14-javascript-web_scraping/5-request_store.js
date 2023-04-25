#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file
const { argv } = require('process');
const request = require('request');
const { writeFile } = require('fs');

const path = argv[3];
const link = argv[2];

request(link, function (err, res, body) {
  if (err) console.log(err);
  else {
    writeFile(path, body, 'utf8', (err) => {
      if (err) console.log(err);
    }
    );
  }
});
