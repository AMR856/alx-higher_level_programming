#!/usr/bin/node
const process = require('process');
const request = require('request');

const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const jsonBody = JSON.parse(body);
  const myObject = {};
  for (let i = 0; i < jsonBody.length; i++) {
    if (jsonBody[i].completed === true) {
      if (myObject[jsonBody[i].userId] === undefined) {
        myObject[jsonBody[i].userId] = 1;
      }
      else {
        myObject[jsonBody[i].userId] = myObject[jsonBody[i].userId] + 1;
      }
    }
  }
  console.log(myObject);
});
