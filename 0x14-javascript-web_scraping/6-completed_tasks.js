#!/usr/bin/node
const process = require('process');
const request = require('request');

const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const jsonBody = JSON.parse(body);
  const myObject = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0 };
  for (let i = 0; i < jsonBody.length; i++) {
    if (jsonBody[i].completed === true) {
      myObject[jsonBody[i].userId] = myObject[jsonBody[i].userId] + 1;
    }
  }
  console.log(myObject);
});
