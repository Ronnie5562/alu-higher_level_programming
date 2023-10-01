#!/usr/bin/node
const fs = require('fs');

const [sourceFilePath1, sourceFilePath2, destinationFilePath] = process.argv.slice(2);
try {
  const content1 = fs.readFileSync(sourceFilePath1, 'utf-8');
  const content2 = fs.readFileSync(sourceFilePath2, 'utf-8');
  fs.writeFileSync(destinationFilePath, content1 + content2);
} catch (error) {
  console.error(error.message);
}
