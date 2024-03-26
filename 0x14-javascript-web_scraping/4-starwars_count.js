#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  let n = 0;
  const films = JSON.parse(body).results;
  for (let i = 0; i < films.length; i++) {
    for (let j = 0; j < films[i].characters.length; j++) {
      if (films[i].characters[j].endsWith('/18/')) {
        n++;
        break;
      }
    }
  }
  console.log(n);
});
