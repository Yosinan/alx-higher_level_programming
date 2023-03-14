#!/usr/bin/node
// a class Rectangle that defines a rectangle

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
	  let i = 0;
	  for (i; i < this.height; i++) {
	    console.log('X'.repeat(this.width));
	  }
  }
}
module.exports = Rectangle;
