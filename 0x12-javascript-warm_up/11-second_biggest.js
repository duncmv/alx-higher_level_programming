#!/usr/bin/node
let maxx = Number.MIN_SAFE_INTEGER;

if (process.argv.length < 4) {
  console.log(0);
} else {
  let max = parseInt(process.argv[2]);
  for (let i = 3; i < process.argv.length; i++) {
    const n = parseInt(process.argv[i]);
    if (n > max) {
      maxx = max;
      max = process.argv[i];
    } else if (n > maxx) {
      maxx = n;
    }
  }
  console.log(maxx);
}
