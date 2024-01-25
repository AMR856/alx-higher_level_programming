#!/usr/bin/node
const process = require('process');
const myCount = Number(process.argv[2]);
if (isNaN(myCount)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < myCount; i++) {
    console.log('C is fun');
  }
}
