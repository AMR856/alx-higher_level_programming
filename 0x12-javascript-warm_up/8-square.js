#!/usr/bin/node
const process = require('process');
const myCount = Number(process.argv[2]);
if (isNaN(myCount)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myCount; i++) {
    console.log('X'.repeat(myCount));
  }
}
