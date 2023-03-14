#!/usr/bin/node
const count = process.argv.length - 1;
console.log(count === 1 ? 'No argument' : count === 2 ? 'Argument found' : 'Arguments found');
