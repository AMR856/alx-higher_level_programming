#!/usr/bin/node
function add (a, b) {
  console.log(String(Number(a) + Number(b)));
}
const process = require('process');
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log('NaN');
} else {
  add(process.argv[2], process.argv[3]);
}
