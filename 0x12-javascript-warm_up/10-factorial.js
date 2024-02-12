#!/usr/bin/node
const num1 = parseInt(process.argv[2]);

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  }
  if (n === 0) {
    return 1;
  }
  const result = n * factorial(n - 1);
  return result;
}

console.log(factorial(num1));
