#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const url = process.argv[2] || '';
const path = process.argv[3];

request(url, (err, res, body) => {
  if (err) {
    return console.log(err);
  }

  fs.writeFile(path, body, 'utf8', (err) => {
    if (err) {
      return console.log(err);
    }
  });
});
