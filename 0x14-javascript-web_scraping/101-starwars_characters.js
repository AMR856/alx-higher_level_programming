#!/usr/bin/node
const process = require('process');
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';
const fullUrl = url.concat('', process.argv[2]);
request(fullUrl, function(error, response, body) {
  if (error) {
    console.log(error);
  }
  const jsonBody = JSON.parse(body);
  for (let i = 0; i < jsonBody.characters.length; i++) {
    request(jsonBody.characters[i], function(err, response1, body1)  {
      if (err) {
        console.log(err);
      }
      console.log(JSON.parse(body1).name);
    });
  }
});
