#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, res, body) {
  if (!err) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, film) => {
      return film.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
