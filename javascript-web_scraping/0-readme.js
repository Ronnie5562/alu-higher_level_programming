#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], function (err, data) {
  err && console.log(err);
  const content = data;
  console.log(content.toString());
});
