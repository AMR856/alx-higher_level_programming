#!/usr/bin/node
const process = require('process');
let myCount = 0;
for (i in process.argv) {
    myCount++;
}
if (myCount == 2) {
    console.log('No argument');
} else {
    console.log(process.argv[2]);
}