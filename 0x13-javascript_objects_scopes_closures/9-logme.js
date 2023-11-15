#!/usr/bin/node
// script to print the num of args already printed and the new arg value
let num = 0;
exports.logMe = function (item) {
  console.log(num + ': ' + item);
  num += 1;
};
