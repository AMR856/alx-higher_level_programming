#!/usr/bin/node
const process = require('process');
const myVar = Number(process.argv[2]);
if (isNaN(myVar)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myVar);
}
