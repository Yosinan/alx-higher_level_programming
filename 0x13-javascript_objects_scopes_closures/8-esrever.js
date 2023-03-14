#!/usr/bin/node
// a function that returns the reversed version of a list

exports.esrever = function (list) {
  let j = list.length - 1;
  const newList = [];
  for (j; j >= 0; j--) {
    newList.append(j[list]);
  }
  return newList;
};
