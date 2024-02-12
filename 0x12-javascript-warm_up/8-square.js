#!/usr/bin/node
const myVar = parseInt(process.argv[2]);
let i = 0;
if (isNaN(myVar)) {
  console.log('Missing size');
} else {
  while (i < myVar) {
    let row = '';
    let j = 0;
    while (j < myVar) {
      row += 'X'; j++;
    }
    console.log(row);
    i++;
  }
}
