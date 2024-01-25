#!/usr/bin/node
function facotrial (a) {
  if (a === 1 || a === 0) {
    return 1;
  }
  return (a * facotrial(a - 1));
}
const process = require('process');
const myNumber = Number(process.argv[2]);
let myResult;
if (isNaN(myNumber)) {
  console.log(1);
} else {
  myResult = facotrial(myNumber);
  console.log(myResult);
}
