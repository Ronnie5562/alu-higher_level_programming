#!/usr/bin/node
const fs = require('fs');
try {
  const fileContent = fs.readFileSync(process.argv[2], 'utf-8');
  console.log(fileContent);
} catch (error) {
  console.log(error.message);
}
