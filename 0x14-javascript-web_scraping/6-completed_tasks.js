#!/usr/bin/node
// script that computes the number of tasks completed by user id
const link = process.argv[2];
const request = require('request');

request(link, (err, res, body) => {
  if (err) console.log(err);
  const totalCompletedTask = {};

  for (let k = 1; k <= 10; k++) {
    const totCompleted = JSON.parse(body).filter(todo => todo.completed === true).filter(todo => todo.userId === k).length;
    while (totCompleted) {
      totalCompletedTask[k] = totCompleted;
      break;
    }
  }
  console.log(totalCompletedTask);
});
