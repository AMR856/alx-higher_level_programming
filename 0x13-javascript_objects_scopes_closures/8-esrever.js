#!/usr/bin/node
exports.esrever = function (list) {
  const myNewList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    myNewList.push(list[i]);
  }
  return myNewList;
};
