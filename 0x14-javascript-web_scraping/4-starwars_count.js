#!/usr/bin/node
const { argv } = require('node:process');
const request = require('request');
const { promisify } = require('util');

const promisedRequest = promisify(request);

async function characterCounter () {
  try {
    const text = await promisedRequest(`${argv[2]}`);

    const body = JSON.parse(text.body);

    let counter = 0;
    // const characterList = [];
    for (const result of body.results) {
      for (const character of result.characters) {
        if (character.slice(-3) === '18/') {
          counter++;
          // characterList.push(promisedRequest(character));
        }
      }
    }

    // const characters = await Promise.all(characterList);

    // for (const char of characters) {
    //   if (JSON.parse(char.body).name === 'Wedge Antilles') { counter++; }
    // }
    console.log(counter);
  } catch (error) {
    console.error('');
  }
}

characterCounter();
