#!/usr/bin/node
const argv = process.argv.slice(2);
const message = argv.length > 0 ? (argv.length === 1 ? 'Argument found' : 'Arguments found') : 'No argument';
console.log(message);
