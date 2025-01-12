#!/usr/bin/node
const { argv } = require('node:process');
function factorial (number) {
  if (number === 1) return (1);
  return (number * factorial(number - 1));
}
if (argv[2] === undefined) console.log(1);
else console.log(factorial(Number(argv[2])));
