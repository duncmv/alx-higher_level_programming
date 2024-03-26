#!/usr/bin/node
const request = require('request');
let url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  const characters = JSON.parse(body).characters;
  for (let i = 0; i < characters.length; i++) {
    url = characters[i];
    request(url, (err, res, body) => {
      if (err) {
        return console.log(err);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
