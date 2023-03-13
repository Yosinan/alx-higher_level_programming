#!/usr/bin/node

const num = Math.floor(Number(process.argv[2]));
function factor (n) {
  let x = 1;
  for (let i = 1; i <= n; i++) {
    x *= i;
  }
  console.log(x);
}
factor(num);
