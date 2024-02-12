#!/usr/bin/node
let maxx;
const { argv } = require('node:process');
if (argv.length < 4) {
  console.log(0);
} else {
  let max = parseInt(argv[2]);
  maxx = parseInt(argv[3]);
  for (let i = 3; i < argv.length; i++) {
    const n = parseInt(argv[i]);
    if (n > max) {
      maxx = max;
      max = argv[i];
    } else if (n > maxx) {
      maxx = n;
    }
  }
}
console.log(maxx);
