#!/usr/bin/node
const { argv } = require('node:process');
const message = argv.length > 2 ? (argv.length === 3 ? 'Argument found' : 'Arguments found') : 'No argument';
console.log(message);
