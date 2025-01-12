#!/usr/bin/node
const { argv } = require('node:process');
if (isNaN(argv[2]) || argv[2] === undefined) console.log('Missing size');
let text = '';
let count = 0;
for (let i = 0; i < Number(argv[2]); i++) text = text + 'X';
while (count < Number(argv[2])) {
  console.log(text);
  count++;
}
