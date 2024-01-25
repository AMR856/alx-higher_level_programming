#!/usr/bin/node
const fs = require('fs');
const AArg = fs.readFileSync(process.argv[2]).toString();
const BArg = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], AArg + BArg);
