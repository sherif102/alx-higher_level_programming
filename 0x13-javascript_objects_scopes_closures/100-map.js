#!/usr/bin/node
const list = require('./test').list;
const nList = list.map((x, counter = 0) => x * counter++);
console.log(list);
console.log(nList);
