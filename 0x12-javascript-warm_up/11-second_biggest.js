#!/usr/bin/node
// a script to search the second biggest integer in the list of arguments
const args = process.argv.slice(2);

function compare (a, b) {
  return a - b;
}

if (args.length === 0) {
  console.log('0');
} else if (args.length === 1) {
  console.log('0');
} else {
  console.log(args.sort(compare)[args.length - 2]);
}
