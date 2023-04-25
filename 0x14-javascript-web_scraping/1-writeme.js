#!/usr/bin/node
// script that writes a string to a file
const { argv } = require('process');
const { writeFile } = require('fs');
const path = argv[2];
const str = argv[3];

writeFile(path, str, 'utf8', function (err) {
  if (err) console.log(err);
});
