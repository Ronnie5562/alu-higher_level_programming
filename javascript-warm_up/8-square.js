#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (isNaN(size)) console.log('Missing size');
else if (size > 0) console.log(('X'.repeat(size) + '\n').repeat(size).trim());
else console.log('Size must be a positive integer');
