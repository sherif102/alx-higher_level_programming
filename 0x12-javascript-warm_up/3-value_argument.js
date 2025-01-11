#!/usr/bin/node
const { argv } = require('node:process');
let argMessage;
if (argv[2] == undefined) argMessage = 'No argument';
else argMessage = argv[2];
console.log(argMessage);
