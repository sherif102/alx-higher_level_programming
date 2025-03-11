#!/usr/bin/node
const { argv } = require('node:process');
const request = require('request');

request(argv[2], function (err, response) {
  if (err) throw err;
  console.log('code:', response.statusCode);
});
