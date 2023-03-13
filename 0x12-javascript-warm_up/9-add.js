#!/usr/bin/node

const num1 = Math.floor(Number(process.argv[2]));
const num2 = Math.floor(Number(process.argv[3]));
function add (a, b) {
  const result = a + b;
  console.log(result);
}

add(num1, num2);
