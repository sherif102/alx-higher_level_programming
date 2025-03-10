#!/usr/bin/node
const { argv } = require('node:process');
const fs = require('fs');

fs.writeFile(argv[2], argv[3], 'utf-8', function (err, file) {
  if (err) throw err;
  console.log(argv[3]);
});
