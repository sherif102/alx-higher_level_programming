#!/usr/bin/node
const { argv } = require('node:process');
const request = require('request');
const { promisify } = require('util');

const promisedRequest = promisify(request);

async function writeFromUrl () {
  const text = await promisedRequest(`${argv[2]}`);

  const body = JSON.parse(text.body);

  const data = {};
  for (const todo of body) {
    if (!data[todo.userId] && todo.completed === true) {
      data[todo.userId] = 1;
    } else if (todo.completed === true) {
      data[todo.userId]++;
    }
  }

  console.log(data);
}

writeFromUrl();
