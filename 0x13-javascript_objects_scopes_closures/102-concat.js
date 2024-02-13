#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;

fs.readFile(argv[2], 'utf-8', (err, first) => {
  if (err) throw err;

  fs.readFile(argv[3], 'utf-8', (err, second) => {
    if (err) throw err;

    const ttt = first + second;
    fs.writeFile(argv[4], ttt, (err) => {
      if (err) throw err;
    });
  });
});
