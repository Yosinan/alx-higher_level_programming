#!/usr/bin/node
//value argument

const value = process.argv;
console.log(typeof value[2] === 'undefined' ? 'No argument' : value[2]);
