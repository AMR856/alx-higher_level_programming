#!/usr/bin/node
const process = require('process');
const request = require('sync-request');

const url = 'https://swapi-api.alx-tools.com/api/films/';
const fullUrl = url.concat('', process.argv[2]);
const response = request('GET', fullUrl);

if (response.statusCode === 200) {
  const jsonBody = JSON.parse(response.getBody('utf8'));

  for (let i = 0; i < jsonBody.characters.length; i++) {
    const characterResponse = request('GET', jsonBody.characters[i]);
    if (characterResponse.statusCode === 200) {
      const characterName = (JSON.parse(characterResponse.getBody('utf8'))).name;
      console.log(characterName);
    } else {
      console.log(`Error fetching character: ${characterResponse.statusCode}`);
    }
  }
} else {
  console.log(`Error fetching film details: ${response.statusCode}`);
}
