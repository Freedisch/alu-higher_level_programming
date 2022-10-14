#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
request('https://swapi-api.hbtn.io/api/films/' + id, (error, res, body) => {
  if (error) return console.log(error);
  console.log(JSON.parse(body).title);
});
