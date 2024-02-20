#!/usr/bin/node
const process = require('process');
const request = require('request');

const url = process.argv[2];
let myCount = 0;
const id = 18;
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const jsonBody = JSON.parse(body);
  for (let i = 0; i < jsonBody.count; i++) {
    for (let j = 0; j < jsonBody.results[i].characters.length; j++) {
      if (jsonBody.results[i].characters[j].includes(id)) {
        myCount = myCount + 1;
      }
    }
  }
  console.log(myCount);
});
