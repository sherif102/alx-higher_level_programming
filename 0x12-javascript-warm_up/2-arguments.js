#!/usr/bin/node
const { argv } = require('node:process');
let argMessage;
if (argv.length === 2) argMessage = 'No argument';
else if (argv.length === 3) argMessage = 'Argument found';
else argMessage = 'Arguments found';
console.log(argMessage);
