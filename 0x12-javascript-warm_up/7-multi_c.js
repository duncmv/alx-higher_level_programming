#!/usr/bin/node
const myVar = parseInt(process.argv[2]);
let i = 0;
if (isNaN(myVar)) {
  console.log('Missing number of occurrences');
} else {
  while (i < myVar) {
    console.log('C is fun');
    i++;
  }
}
