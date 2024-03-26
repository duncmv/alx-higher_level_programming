#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;

fs.readFile(argv[2], 'utf-8', (err, filecontent) => {
  if (err) {
    return console.log(err);
  }
  console.log(filecontent);
});
