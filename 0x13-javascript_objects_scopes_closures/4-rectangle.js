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
    for (let j = 0; j < this.height; j++) {
      let string = '';
      for (let p = 0; p < this.width; p++) {
	string += 'X';
      }
      console.log(string);
      string = '';
    }
  }

  rotate () {
    const width = this.width;
    this.width = this.height;
    this.height = width;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
