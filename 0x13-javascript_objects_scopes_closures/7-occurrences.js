#!/usr/bin/node
// a function that returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  let j = 0;
  for (j; j < list.length; j++) {
    if (list[j] === searchElement) {
      counter++;
    }
  }
  return counter;
};
