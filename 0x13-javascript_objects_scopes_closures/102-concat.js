#!/usr/bin/node
const { argv } = require('node:process');
const fs = require('fs');
const file1 = argv[2];
const file2 = argv[3];
const file3 = argv[4];

fs.open(file1, 'r', (err, filea) => {
  if (err) throw (err);
  fs.readFile(filea, (err, data) => {
    if (err) throw (err);
    fs.appendFile(file3, data, () => console.log('Done'));
  });
});
fs.open(file2, 'r', (err, filea) => {
  if (err) throw (err);
  fs.readFile(filea, (err, data) => {
    if (err) throw (err);
    fs.appendFile(file3, data, () => console.log('Done'));
  });
});
