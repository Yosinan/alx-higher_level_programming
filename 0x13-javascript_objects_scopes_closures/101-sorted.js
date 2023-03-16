#!/usr/bin/node
// a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence
const dict = require('./101-data.js').dict;
const newDic = {};
for (const key in dict) {
  if (newDic[dict[key]] === undefined) {
    newDic[dict[key]] = [];
  }
  newDic[dict[key]].push(key);
}
console.log(newDic);
