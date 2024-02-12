#!/usr/bin/node
const num1 = parseInt(process.argv[2]);
if (isNaN(num1)) {
  console.log(1);
}
function factorial (n) {
  if (n === 0) {
    return 1;
  }
  const result = n * factorial(n - 1);
  return result;
}

console.log(factorial(num1));
