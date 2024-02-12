#!/usr/bin/node
const { argv } = require('node:process');

const myVar = parseInt(argv[2]);

if (!isNaN(myVar)) {
  console.log(`My number: ${myVar}`);
} else {
  console.log('Not a number');
}
