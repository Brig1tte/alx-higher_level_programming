#!/usr/bin/node
// a script to export a function that executes a function x times
exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
