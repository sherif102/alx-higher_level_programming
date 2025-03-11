#!/usr/bin/node
const { argv } = require('node:process');
const request = require('request');
const { promisify } = require('util');

const promisedRequest = promisify(request);

async function characterCounter () {
  try {
    const text = await promisedRequest(`https://swapi-api.alx-tools.com/api/films/${argv[2]}`);

    const body = JSON.parse(text.body);

    const peopleList = [];
    for (const people of body.characters) {
      peopleList.push(promisedRequest(people));
    }

    const peoples = await Promise.all(peopleList);

    for (const person of peoples) {
      console.log(JSON.parse(person.body).name);
    }
  } catch (error) {
    console.error('');
  }
}

characterCounter();
