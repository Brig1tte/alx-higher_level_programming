#!/usr/bin/node
// a script to export a function that executes a function x times
exports.callMeMoby = function (x, theFunction) {
  for (let j = 0; j < x; j++) {
    theFunction();
  }
};
