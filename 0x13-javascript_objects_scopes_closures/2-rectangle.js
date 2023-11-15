#!/usr/bin/node
// a class Rectangle that defines a rectangle:
module.exports = class Rectangle {
	constructor(h = 0, w = 0) {
		if (h >= 0 || w >= 0) {
		} else {
			this.height = h;
			this.width = w;
		}
	}
};
