#!/usr/bin/node
const { argv } = require('node:process');
let fb = 0;
let sb = 0;
for (let i = 2; i < argv.length; i++) {
  if (Number(argv[i]) > fb) {
    sb = fb;
    fb = Number(argv[i]);
  } else if (Number(argv[i] > sb)) sb = Number(argv[i]);
}
console.log(sb);
