#!/usr/bin/node
// a script to print two arguments passed to it in the "is" format
const args = process.argv.slice(2);
console.log(args[0] + ' is ' + args[1]);
