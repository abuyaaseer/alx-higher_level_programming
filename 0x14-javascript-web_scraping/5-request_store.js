#!/usr/bin/node

const Request = require('request');
const fs = require('fs');

Request(process.argv[2], function (err, response, body) {
  if (err == null) {
    fs.writeFileSync(process.argv[3], body);
  }
});
