#!/usr/bin/node
// script that reads and prints the content of a file
// importing built-in modules
const { readFile } = require('fs');
const { argv } = require('process');
const path = argv[2];

readFile(path, 'utf8', function (err, data) {
  if (err) console.log(err);
  else console.log(data);
});
