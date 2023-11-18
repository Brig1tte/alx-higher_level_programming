#!/usr/bin/node
// a function to convert a num from base10 to another base passed as arg:
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
