#!/usr/bin/node
let myArgCount = 0;
exports.logMe = function (item) {
  console.log(myArgCount + ': ' + item);
  myArgCount++;
};
