#!/usr/bin/node
// a class Square to define a square and inherits from 5-square.js:
const Square5 = require('./5-square');
module.exports = class Square extends Square5 {
  constructor (size = 0) {
    super(size);
  }

  charPrint (c) {
    if (typeof c === 'undefined') {
      this.print();
    } else {
      let string = '';
      for (let j = 0; j < this.height; j++) {
        for (let p = 0; p < this.width; p++) {
          string += c;
        }
        console.log(string);
        string = '';
      }
    }
  }
};
