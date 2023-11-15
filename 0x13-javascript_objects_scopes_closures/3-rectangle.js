#!/usr/bin/node
// a class Rectangle that defines a rectangle:
module.exports = class Rectangle {
	constructor (w = 0, h = 0) {
		if (w <= 0 || h <= 0) {
		} else {
			this.width = w;
			this.height = h;
		}
	}

	print () {
		let string = '';
		for (let j = 0; j < this.height; j++) {
			for (let p = 0; p < this.width; p++) {
				string += 'X'
			}
			console.log(string);
			string = '';
		}
	}
};
