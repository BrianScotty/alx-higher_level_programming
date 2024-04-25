#!/usr/bin/node

const request = require('request');
// Import 'request' module.

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
// Construct the URL for the specific Star Wars film.

request(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
