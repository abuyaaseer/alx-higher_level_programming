#!/usr/bin/node
console.log((typeof process.argv[2] === 'undefined' ? 'undefined' : process.argv[2]) + ' is ' + (typeof process.argv[3] === 'undefined' ? 'undefined' : process.argv[3]));
