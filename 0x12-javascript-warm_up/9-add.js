#!/usr/bin/node
function add (a, b) {
  const c = Number(a) + Number(b);
  console.log(c);
}
const process = require('process');
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(NaN);
} else {
  add(process.argv[2], process.argv[3]);
}
