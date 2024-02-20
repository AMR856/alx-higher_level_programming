#!/usr/bin/node
const process = require('process');
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  fs.writeFile(filePath, body, err => {
    if (err) {
      console.error(err);
    } else {
      /* File was written succesfully  */
    }
  });
});
