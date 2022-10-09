#!/usr/bin/node
const string = "C is fun";
if(process.argv[2] === undefined) console.log("Missing number of occurrences");
else string.forEach((value, index) => console.log(string[index]));