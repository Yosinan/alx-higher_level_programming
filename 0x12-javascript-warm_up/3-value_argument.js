#!/usr/bin/node

const value = process.argv;
console.log(typeof value[2] === 'undefined' ? 'No argument' : value[2]);
