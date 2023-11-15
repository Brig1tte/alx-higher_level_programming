#!/usr/bin/node
// a class Rectangle that defines a rectangle:
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let string = '';
    for (let j = 0; j < this.height; j++) {
      for (let p = 0; p < this.width; p++) {
	string += 'X';
      }
      console.log(string);
    }
  }
}

module.exports = Rectangle;
