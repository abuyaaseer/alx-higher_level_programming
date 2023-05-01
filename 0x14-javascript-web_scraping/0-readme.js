#!/usr/bin/node

const fs = require('fs');
const Name = process.argv[2];

fs.readFile(Name, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
