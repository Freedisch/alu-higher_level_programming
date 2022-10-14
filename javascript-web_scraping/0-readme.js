#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', (err, result) => {
  if (err) return console.log(err);
  else return console.log(result);
});
