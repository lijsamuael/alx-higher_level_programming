#!/usr/bin/node
const firstArg = process.argv[2];
console.log(firstArg === undefined ? 'No argument' : firstArg);
