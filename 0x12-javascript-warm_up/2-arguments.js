#!/usr/bin/node
// a script to print a message dependent on numb of args passed:
// messages: "No argument", "Argument found"

const argsNum = process.argv.slice(2).length;
if (argsNum === 0) {
	console.log('No argument');
} else if (argsNum === 1) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
