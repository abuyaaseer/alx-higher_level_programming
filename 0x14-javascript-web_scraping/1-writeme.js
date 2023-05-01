#!/usr/bin/node

const fs = require('fs');
const Name = process.argv[2];
const string = process.argv[3];

fs.writeFile(Name, string, 'utf-8', function (err) {
  if (err) console.log(err);
});
