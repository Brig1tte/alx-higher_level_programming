#!/usr/bin/node
// a class Square to define a square and inherits from 4-rectangle.js:
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size = 0) {
    super(size, size);
  }
};
