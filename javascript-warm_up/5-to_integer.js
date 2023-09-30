#!/usr/bin/node
const argv = process.argv.slice(2);
console.log(parseInt(argv[0]) ? `My number: ${parseInt(argv[0])}` : 'Not a number');
