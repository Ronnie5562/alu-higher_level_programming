#!/usr/bin/node
const argv = process.argv.slice(2);
const message = argv.length > 0 ? argv[0] : 'No argument';
console.log(message);
