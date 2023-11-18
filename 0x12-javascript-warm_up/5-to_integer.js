#!/usr/bin/node
// a script to print My number if 1st arg can be converted to an int

if (parseInt(process.argv[2])) {
  console.log(`My number: ${parseInt(process.argv[2])}`);
} else {
  console.log('Not a number');
}
