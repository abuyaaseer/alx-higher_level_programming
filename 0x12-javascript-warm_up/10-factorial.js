#!/usr/bin/node
function factorial (x) {
  if (isNaN(x) || x === 0) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}

const arg = Number(process.argv[2]);
console.log(factorial(arg));
