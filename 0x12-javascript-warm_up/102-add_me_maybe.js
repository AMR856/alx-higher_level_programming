#!/usr/bin/node
exports.addMeMaybe = function (myNumber, myFun) {
  myNumber++;
  myFun(myNumber);
};
