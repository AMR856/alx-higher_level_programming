#!/usr/bin/node
const importedArray = require('./100-data').list;
const theResultArray = importedArray.map(function (element, index) {
  return element * index;
});
console.log(importedArray);
console.log(theResultArray);
