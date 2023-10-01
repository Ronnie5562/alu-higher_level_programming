#!/usr/bin/node

const inputDictionary = require('./101-data').dict;

const reversedDictionary = {};
for (const [key, value] of Object.entries(inputDictionary)) {
  if (reversedDictionary[value] === undefined) {
    reversedDictionary[value] = [key];
  } else {
    reversedDictionary[value].push(key);
  }
}
console.log(reversedDictionary);
