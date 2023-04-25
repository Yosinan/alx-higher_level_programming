#!/usr/bin/node
# script that reads and prints the content of a file
// importing built-in modules
const read_file = require('fs');
const argv = require('process');
const path = argv[2];

read_file(path, 'utf8', function (err, data) {
	if (err) console.log(err);
	else console.log(data);
});
