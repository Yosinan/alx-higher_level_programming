#!/usr/bin/node

const size = process.argv.length;
if (size <= 3) {
  console.log(0);
} else {
  const argu = process.argv.map(Number).slice(2, size).sort((a, b) => a - b);
  console.log(argu[argu.length - 2]);
}
