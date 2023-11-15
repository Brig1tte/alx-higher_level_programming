#!/usr/bin/node
// a class Rectangle that defines a rectangle:
class Rectangle {
  constructor(w, h) {
    if (h > 0 || w > 0) {
      this.height = h;
      this.width = w;
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
