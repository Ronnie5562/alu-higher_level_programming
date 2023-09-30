#!/usr/bin/node
let max = 0;
let secondMax = 0;
for (const num of process.argv.slice(2).map(Number)) {
  if (num > max) {
    secondMax = max;
    max = num;
  }
  if (num > secondMax && max > num) {
    secondMax = num;
  }
}
console.log(secondMax);
