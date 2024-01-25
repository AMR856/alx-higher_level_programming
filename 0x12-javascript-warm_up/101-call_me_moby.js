#!/usr/bin/node
exports.callMeMoby = function (myNumber, myFun) {
  for (let i = 0; i < myNumber; i++) {
    myFun();
  }
};
