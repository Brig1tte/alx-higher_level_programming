#!/usr/bin/node
// a script that prints a square

const size = parseInt(process.argv[2]);
// if not a number
if (!size) {
  console.log('Missing size');
} else {
  for (let j = 0; j < size; j++) {
    let rows = '';
    for (let k = 0; k < size; k++) {
      rows += 'X';
    }
    console.log(rows);
  }
}
