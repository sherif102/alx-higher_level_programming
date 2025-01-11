#!/usr/bin/node
const { argv } = require('node:process');
let argMessage;
if (argv[2] === undefined) argMessage = 'Not a number';
else if (isNaN(argv[2])) argMessage = 'Not a number';
else argMessage = `My number: ${Number(argv[2])}`;
console.log(argMessage);
