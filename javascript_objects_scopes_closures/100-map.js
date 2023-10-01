#!/usr/bin/node
const arr = require('./100-data.js').list;
const newArr = arr.map((data, index) => index * data);
console.log(arr);
console.log(newArr);
