#!/usr/bin/node
const process = require('process');
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';
const fullUrl = url.concat('', process.argv[2]);
request(fullUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  console.log(JSON.parse(body).title);
});
