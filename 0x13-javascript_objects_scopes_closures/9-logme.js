#!/usr/bin/node
exports.logMe = function (item) {
  let myArgCount = 0;
  function printer (newItem) {
    console.log(myArgCount + ': ' + newItem);
  }
  myArgCount++;
  return printer;
};
