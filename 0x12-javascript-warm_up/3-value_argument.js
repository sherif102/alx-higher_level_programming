#!/usr/bin/node
const { argv } = require('node:process');
let argMessage;
if (argv.length < 3) argMessage = 'No argument';
else argMessage = argv[2];
console.log(argMessage);
