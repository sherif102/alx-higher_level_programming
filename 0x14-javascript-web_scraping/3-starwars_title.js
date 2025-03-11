#!/usr/bin/node
const { argv } = require('node:process');
const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${argv[2]}`, function (err, response) {
  if (err) throw err;
  const body = JSON.parse(response.body);
  console.log(body.title);
});
