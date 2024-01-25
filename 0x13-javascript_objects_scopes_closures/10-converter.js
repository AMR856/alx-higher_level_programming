#!/usr/bin/node
exports.converter = function (base) {
  return function (myNum) {
    return myNum.toString(base);
  };
};
