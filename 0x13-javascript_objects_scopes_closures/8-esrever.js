#!/usr/bin/node
// a function to return the reversed version of a list:
exports.esrever = function (list) {
  if (Array.isArray(list)) {
    const listCopy = [];
    list.forEach(element => listCopy.unshift(element));
    return listCopy;
  }
};
