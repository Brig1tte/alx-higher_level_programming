#!/usr/bin/node
// a script to print x times "C is fun"

if (!process.argv[2]) {
  console.log('Missing number of occurrences');
} else {
  const times = parseInt(process.argv[2]);
  for (let j = 0; j < times; j++) {
    console.log('C is fun');
  }
}
