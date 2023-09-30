#!/usr/bin/node
const argv = process.argv.slice(2);
const message = argv[0] ? argv[0] : 'No argument';
console.log(message);
