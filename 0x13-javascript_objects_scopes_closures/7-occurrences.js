#!/usr/bin/Node
// a function to return the number of occurrences in a list:
exports.nbOccurences = function (list, searchElement) {
  if (Array.isArray(list)) {
    let occurrences = 0;
    for (let j = 0; j < list.length; j++) {
      if (searchElement === list[j]) {
        occurrences += 1;
      }
    }
    return occurrences;
  }
};
