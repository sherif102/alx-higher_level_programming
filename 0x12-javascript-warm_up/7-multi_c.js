#!/usr/bin/node
const { argv } = require('node:process');
if (isNaN(argv[2]) || argv[2] === undefined) console.log('Missing number of occurrences');
let count = 0;
while (count < Number(argv[2])) {
  console.log('C is fun');
  count++;
}
