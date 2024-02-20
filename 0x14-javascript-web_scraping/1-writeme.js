#!/usr/bin/node
const process = require('process');
const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, err => {
  if (err) {
    console.error(err);
  } else {
    /* File was written succesfully  */
  }
});
