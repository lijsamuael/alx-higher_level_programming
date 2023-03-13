#!/usr/bin/node
const count = process.argv.slice(2).length;
console.log(count === 0 ? 'No argument' : count === 1 ? 'Argument found' : 'Arguments found');
