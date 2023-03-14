#!/usr/bin/node
// a script that imports an array and computes a new array

const list = require('./100-data.js').list;
console.log(list);

const newList = list.map((y, indice) => (y * indice)
);
console.log(newList);
