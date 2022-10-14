#!/usr/bin/node

const request = require('request');

request(process.argv[2], (error, res) => {
  if (error) {
    console.error(error);
  }
  console.log('code:', res && res.statusCode);
});
