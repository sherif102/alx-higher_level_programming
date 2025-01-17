#!/usr/bin/node
const dict = require('./test').dict;
const nDict = {};
for (const [key, value] of Object.entries(dict)) {
  if (nDict[value] === undefined) {
    nDict[value] = [key];
  } else {
    nDict[value].push(key);
  }
}
console.log(nDict);
