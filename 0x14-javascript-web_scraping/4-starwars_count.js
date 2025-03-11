#!/usr/bin/node
const request = require('request');
const { promisify } = require('util');

const promisedRequest = promisify(request);

async function characterCounter () {
  const text = await promisedRequest('https://swapi-api.alx-tools.com/api/films/');

  const body = JSON.parse(text.body);

  let counter = 0;
  const characterList = [];
  for (const result of body.results) {
    for (const character of result.characters) {
      characterList.push(promisedRequest(character));
    }
  }

  const characters = await Promise.all(characterList);

  for (const char of characters) {
    if (JSON.parse(char.body).name === 'Wedge Antilles') { counter++; }
  }
  console.log(counter);
}

characterCounter();
