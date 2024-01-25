#!/usr/bin/node
const process = require('process');
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  const myArray = process.argv.slice(2);
  const numberArray = [];
  for (let i = 0; i < myArray.length; i++) {
    numberArray.push(parseInt(myArray[i]));
  }
  numberArray.sort();
  console.log(numberArray[numberArray.length - 2]);
}
