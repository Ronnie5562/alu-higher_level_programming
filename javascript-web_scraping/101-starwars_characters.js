#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;
request(url, function (err, res, body) {
  if (!err) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

function printCharacters (characters, index) {
  request(characters[index], function (err, res, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}
