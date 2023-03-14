#!/usr/bin/node
/*
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let j = 0;
    for (j; j < this.height; j++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
	  this.width = h;
	  this.height = w;
  }

  double () {
	  this.width = w * 2;
	  this.height = h * 2;
  }
}
module.exports = Rectangle;
*/
const Rectangle = require('./4-rectangle');

const r1 = new Rectangle(2, 3);
console.log('Normal:');
r1.print();

console.log('Double:');
r1.double();
r1.print();

console.log('Rotate:');
r1.rotate();
r1.print();
