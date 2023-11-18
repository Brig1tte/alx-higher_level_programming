#!/usr/bin/node
// a script to compute and print a factorial
let num = process.argv[2];

if (!num) {
  num = 0;
}

function factorial (num) {
  if (num === 0) {
    return (1);
  } else {
    return (num * factorial(num - 1));
  }
}

console.log(factorial(num));
