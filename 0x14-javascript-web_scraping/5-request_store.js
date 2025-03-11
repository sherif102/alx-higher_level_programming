#!/usr/bin/node
const { argv } = require('node:process');
const request = require('request');
const { promisify } = require('util');
const fs = require('fs');

const promisedRequest = promisify(request);

async function writeFromUrl () {
  const text = await promisedRequest(`${argv[2]}`);

  const body = text.body;

  fs.writeFile(argv[3], body, 'utf-8', function (err, done) {
    if (err) throw err;
    console.log('');
  });
}

writeFromUrl();
