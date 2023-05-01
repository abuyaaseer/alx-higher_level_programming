#!/usr/bin/node

const Request = require('request');
const URL = process.argv[2];

Request(URL, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
