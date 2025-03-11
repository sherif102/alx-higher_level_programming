#!/usr/bin/node
const { argv } = require('node:process');
const request = require('request');

request(argv[2], function (error, response) {
  console.error('error:', error);
  console.log('code:', response.statusCode);
});
