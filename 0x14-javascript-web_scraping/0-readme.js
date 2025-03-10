#!/usr/bin/node
const { argv } = require('node:process');
const fs = require('fs');

fs.readFile(argv[2], 'utf-8', function (err, file) {
  if (err) throw err;
  console.log(file);
});
